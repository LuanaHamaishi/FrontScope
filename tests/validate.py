"""Validação offline do perfil de empacotamento usado neste repositório (stdlib).

Não é parser YAML geral nem substitui skills-ref ou teste comportamental.
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
        return ['SKILL.md sem frontmatter delimitado ou corpo.']
    # Perfil deliberadamente restrito: strings simples em name/description,
    # mapa metadata de strings, sem aliases, tags ou outros recursos YAML.
    fields = {}
    metadata = {}
    in_metadata = False
    for line in match[1].splitlines():
        if line == 'metadata:':
            if in_metadata:
                errors.append('metadata duplicado.')
            in_metadata = True
            continue
        item = re.fullmatch(r'(  )?([a-z][a-z-]*): (.+)', line)
        if not item or bool(item[1]) != in_metadata:
            errors.append(f'Linha fora do perfil YAML suportado: {line!r}')
            continue
        key, value = item[2], item[3]
        target = metadata if in_metadata else fields
        if key in target:
            errors.append(f'Chave duplicada: {key}')
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                errors.append(f'String inválida: {key}')
        elif (': ' in value or ' #' in value or value[0] in "'[{&*!|>" or
              value.lower() in {'true', 'false', 'null', '~'} or
              re.fullmatch(r'[\d.+-]+', value)):
            errors.append(f'String deve ser explícita no perfil local: {key}')
        if not isinstance(value, str) or not value.strip():
            errors.append(f'Valor não é string preenchida: {key}')
        target[key] = value
    if set(fields) != {'name', 'description'}:
        errors.append('Perfil requer exatamente name e description, além de metadata opcional.')
    name = fields.get('name', '')
    if not (1 <= len(name) <= 64 and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name)):
        errors.append('Nome inválido.')
    if name != SKILL.name:
        errors.append('Nome diverge do diretório.')
    if not 1 <= len(fields.get('description', '')) <= 1024:
        errors.append('Descrição fora do limite.')
    if len(source.splitlines()) >= 500:
        errors.append('Entrypoint excede recomendação de 500 linhas.')

    # Links Markdown locais fora de blocos de código. Não acessa rede.
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
                errors.append(f'Link local inválido em {document.relative_to(ROOT)}: {raw}')
            if document.is_relative_to(SKILL) and not target.is_relative_to(SKILL):
                errors.append(f'Recurso do pacote depende de arquivo externo: {raw}')

    cases = json.loads((ROOT / 'tests' / 'cases.json').read_text(encoding='utf-8'))
    ids = set()
    for case in cases:
        if not case['id'] or case['id'] in ids:
            errors.append('ID de cenário vazio/duplicado.')
        ids.add(case['id'])
        if not case['prompt'] or not case['accept'] or not case['reject'] or not case['inputs']:
            errors.append(f'Cenário incompleto: {case["id"]}')
        for resource in case['inputs']:
            target = (ROOT / 'tests' / resource).resolve()
            if not target.is_relative_to(ROOT / 'tests') or not target.is_file():
                errors.append(f'Fixture inválido: {resource}')
    print(f'Inspecionados: {len(documents)} documentos, {checked_links} links locais, {len(cases)} cenários.')
    return errors


if __name__ == '__main__':
    failures = validate()
    for failure in failures:
        print(f'ERRO: {failure}')
    if not failures:
        print('OK: perfil de frontmatter, nome/diretório, recursos e manifesto de avaliações.')
        print('Não comprova execução de skill, comportamento do modelo ou YAML arbitrário.')
    sys.exit(bool(failures))
