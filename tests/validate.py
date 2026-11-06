"""Offline validation of this repository's packaging profile (stdlib).

Not a general YAML parser or a replacement for skills-ref or behavior evaluation.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents' / 'skills' / 'frontscope'


def validate():
    errors = []
    source = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---\n(.+)', source, re.S)
    if not match:
        return ['SKILL.md is missing delimited frontmatter or a body.']
    # Deliberately restricted profile: simple name/description strings and a
    # metadata string map; no aliases, tags, or other YAML features.
    fields = {}
    metadata = {}
    in_metadata = False
    for line in match[1].splitlines():
        if line == 'metadata:':
            if in_metadata:
                errors.append('Duplicate metadata mapping.')
            in_metadata = True
            continue
        item = re.fullmatch(r'(  )?([a-z][a-z-]*): (.+)', line)
        if not item or bool(item[1]) != in_metadata:
            errors.append(f'Line outside the supported YAML profile: {line!r}')
            continue
        key, value = item[2], item[3]
        target = metadata if in_metadata else fields
        if key in target:
            errors.append(f'Duplicate key: {key}')
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                errors.append(f'Invalid string: {key}')
        elif (': ' in value or ' #' in value or value[0] in "'[{&*!|>" or
              value.lower() in {'true', 'false', 'null', '~'} or
              re.fullmatch(r'[\d.+-]+', value)):
            errors.append(f'An explicit string is required by the local profile: {key}')
        if not isinstance(value, str) or not value.strip():
            errors.append(f'Value must be a nonempty string: {key}')
        target[key] = value
    if set(fields) != {'name', 'description'}:
        errors.append('Profile requires exactly name and description, plus optional metadata.')
    name = fields.get('name', '')
    if not (1 <= len(name) <= 64 and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)):
        errors.append('Invalid name.')
    if name != SKILL.name:
        errors.append('Name does not match the directory.')
    if not 1 <= len(fields.get('description', '')) <= 1024:
        errors.append('Description length is outside the allowed range.')
    if len(source.splitlines()) >= 500:
        errors.append('Entry point exceeds the 500-line recommendation.')

    # Local Markdown links outside code blocks. No network access.
    documents = [ROOT / 'README.md', *SKILL.rglob('*.md'), * (ROOT / 'tests').glob('*.md')]
    checked_links = 0
    for document in documents:
        content = document.read_text(encoding='utf-8')
        content = re.sub(r'^```.*?^```[^\n]*$', '', content, flags=re.M | re.S)
        for raw in re.findall(r'\[[^\]]+\]\(([^)]+)\)', content):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', raw) or raw.startswith('#'):
                continue
            target = (document.parent / unquote(raw.split('#')[0].strip('<>'))).resolve()
            checked_links += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'Invalid local link in {document.relative_to(ROOT)}: {raw}')
            if document.is_relative_to(SKILL) and not target.is_relative_to(SKILL):
                errors.append(f'Package resource depends on an external file: {raw}')

    cases = json.loads((ROOT / 'tests' / 'cases.json').read_text(encoding='utf-8'))
    ids = set()
    expected_spec_tests = {f'T{number:02d}' for number in range(1, 13)}
    covered_spec_tests = set()
    for case in cases:
        if not case['id'] or case['id'] in ids:
            errors.append('Empty or duplicate case ID.')
        ids.add(case['id'])
        if not case['prompt'] or not case['accept'] or not case['reject'] or not case['inputs']:
            errors.append(f'Incomplete case: {case["id"]}')
        spec_tests = case.get('spec_tests', [])
        if (not isinstance(spec_tests, list) or not spec_tests or
                any(not isinstance(test, str) or test not in expected_spec_tests for test in spec_tests)):
            errors.append(f'Invalid specification mapping: {case["id"]}')
        else:
            covered_spec_tests.update(spec_tests)
        for resource in case['inputs']:
            target = (ROOT / 'tests' / resource).resolve()
            if not target.is_relative_to(ROOT / 'tests') or not target.is_file():
                errors.append(f'Invalid fixture: {resource}')
    missing_spec_tests = expected_spec_tests - covered_spec_tests
    if missing_spec_tests:
        errors.append(f'Specification scenarios without mapped fixtures: {", ".join(sorted(missing_spec_tests))}')
    print(f'Inspected: {len(documents)} documents, {checked_links} local links, {len(cases)} cases.')
    return errors


if __name__ == '__main__':
    failures = validate()
    for failure in failures:
        print(f'ERROR: {failure}')
    if not failures:
        print('OK: frontmatter profile, name/directory, resources, and evaluation manifest.')
        print('Does not establish skill execution, model behavior, or arbitrary YAML validity.')
    sys.exit(bool(failures))
