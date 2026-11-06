# Validation record — v0.1.0

Date: November 6, 2026 (America/Sao_Paulo). Local checks executed in the Windows/PowerShell workspace. No package installation was needed. Earlier records below retain their original scope and counts; they are not claims of current behavioral evaluation.

## Initial implementation evidence

| Command/check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documents, 36 local links, eight cases; frontmatter profile, name/directory, links, resource isolation, and manifest validated; exit 0 |
| `node tests/check-fixtures.mjs` | Regression reproduced: base returns 100 and candidate 90 for zero discount; four other inputs compared; clean control outputs equal for five inputs; exit 0 |
| `python -X utf8 tests/probe_codex.py` | Native `skills/list` discovery: `name=frontscope`, `scope=repo`, `enabled=true`, path to `.agents/skills/frontscope/SKILL.md`; no model turn; exit 0 |
| `git diff --check` | No whitespace errors in tracked changes; exit 0. New files also received local whitespace inspection |
| Isolated validator experiment through Python/stdin | Intact temporary copy accepted; mismatched name and missing referenced resource rejected. Original files preserved; exit 0 |

Observed binary: `codex-cli 0.164.0-alpha.11.1`. Discovery was first queried directly through the local protocol and then exposed in the reproducible probe. It checks this repository's path, not another installation with the same name. The native parser accepted metadata and enabled the skill.

To reproduce the negative experiment, copy the package, README, and tests to a temporary directory and run that copy's validator: intact package (expected 0), then a different `name` from the directory (expected 1); restore the file and rename `references/context.md` (expected 1). Do not change the active installation for this experiment. These are integrity checks, not agent behavior evaluations.

## Specification additions — November 6, 2026

Four fixtures and rubrics were added: a local hook with one consumer, monorepo impact, unsafe legacy precedent, and sensitive synthetic enterprise material. The manifest now has 12 cases explicitly mapped to T01–T12; the mapping is not one-to-one. Report contract/examples gained finding IDs and an ordered plan where appropriate. T10 evaluation requires before/after inventory/hashes and tool-activity inspection.

| Executed command/check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documents, 46 local links, 12 cases; valid package profile, references, manifest, and T01–T12 mapping coverage; exit 0 |
| `node tests/check-fixtures.mjs` | Zero-discount regression reproduced and clean control preserved for checked inputs; exit 0 |
| `python -X utf8 tests/probe_codex.py` | `frontscope` enabled at this repository's path with `repo` scope; no model turn; exit 0 |
| Experiment in temporary copies through Python/stdin | Complete mapping accepted; missing T12 and nonexistent T99 rejected; exit 0 |
| `git diff --check` and new-fixture whitespace inspection | No whitespace errors |

To reproduce the mapping experiment, use a temporary copy: validate the intact manifest (expected 0), remove `sensitive-material` to leave T12 uncovered (expected 1), restore it, then replace one `spec_tests` with `["T99"]` (expected 1). This checks matrix integrity, not model judgment. New fixtures were inspected statically; no payload, framework app, browser, or enterprise flow was executed.

## English default

At the owner's request, English replaces the initial Brazilian Portuguese default. The entry point now declares `metadata.language: en` and English reports/explanations by default, with explicit user language overrides. References, report template, fixtures, prompts/rubrics, guided reports, development instructions, and validator/probe messages are in English. Sample UI strings in the synthetic fixtures were translated consistently on both sides of the clean diff. Existing application text remains protected by the skill's instruction to preserve it unless translation is authorized.

The following checks were rerun for this revision:

| Command/check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documents, 46 local links, 12 cases; package profile and T01–T12 mapping valid; exit 0; validator output in English |
| `node tests/check-fixtures.mjs` | Zero-discount regression reproduced and clean control equivalent for five inputs; exit 0; output in English |
| `python -X utf8 tests/probe_codex.py` | Updated skill found enabled at the repository path with `repo` scope; exit 0; probe output in English; no model turn |
| `git diff --check` | No whitespace errors in tracked changes |
| Static review and targeted language search | Entry point and report template default to English; previous Portuguese-default instructions removed; explicit language overrides remain documented |

These outcomes do not establish language selection by a model; English-default and explicit-language-override behavior still need fresh-session evaluation as described in the guide. The optional skill-creator validator was skipped again because PyYAML remains unavailable; no dependency was installed.

## What these checks do not establish

- The 12 current cases have inputs and rubrics, but have not been run as an independent model evaluation suite in fresh sessions. The original eight cases remain represented. Three guided reports in [examples.md](examples.md) demonstrate regression, clean control, and fallback; they are not blind evaluations.
- No integrated review in a fresh Codex/VS Code session, automatic selection test, or Copilot/Claude Code discovery/execution was performed. End-to-end compatibility remains unverified.
- React/Vue are decision-evaluation code fixtures; components were not mounted in a framework. Angular/Svelte have references without dedicated execution.
- Browser execution, screenshots, visual comparison, profiling, and security/dependency scans were not performed. There is no approved baseline or complete accessibility result.
- `skills-ref` was not run. The local validator is restricted to this package's YAML profile. The skill-creator `quick_validate.py` was not run because PyYAML was missing (`importlib.util.find_spec('yaml')` returned false); nothing was installed for this optional tool.
- JavaScript fixture checks are not an application test suite or proof of correct repository reviews.

Follow the [evaluation procedure](README.md) to run cases in actual agents with identical inputs and separate rubrics.
