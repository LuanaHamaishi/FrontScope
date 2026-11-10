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

## Initial test policy draft — November 9, 2026 (superseded)

Branch: `feat/existing-test-validation`, created from `c2fe3a3`. An initial draft added existing-test discovery, baseline where feasible, post-change execution, and commit-readiness checks, but its treatment of new/updated tests was too restrictive. The user clarified that testing must follow intended behavior and project context. This draft has been superseded by the contextual correction below; its check results remain historical evidence, not current policy.

The separate `tests/test-validation-cases.json` adds five policy cases without modifying the original twelve cases or executable checks. They cover unchanged existing tests, absent suites, missing direct coverage/stale results, blocked tooling, and intentional contract conflicts. No supplementary behavioral case has been executed by an independent model.

| Executed command/check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documents, 51 local links, original 12 cases valid; exit 0 |
| `node tests/check-fixtures.mjs` | Existing regression/control checks unchanged and passing; exit 0 |
| Supplementary manifest integrity inspection through Python/stdin | Five unique cases with complete prompts/rubrics and existing input paths |
| Isolated `node --test tests/total.test.mjs` experiment | Base: exit 0; regressed candidate: exit 1; corrected source: exit 0; test bytes remained identical by SHA-256 in all three runs |
| `python -X utf8 tests/probe_codex.py` | Updated skill found enabled at the repository path with `repo` scope; exit 0; no model turn |
| Comparison against committed test resources | All 20 preexisting test/fixture/script/manifest files unchanged; new evaluation resources have no trailing whitespace |
| `git diff --check` | No whitespace errors in tracked changes |

For the isolated experiment, an evaluator copied the new synthetic existing test into a temporary project and selected source from `fixtures/regression/before.mjs`, then `after.mjs`, then the corrected base implementation. Only the temporary `src/total.mjs` changed between runs. The intentionally failing candidate establishes regression detection; it is not an unresolved failure in FrontScope's executable checks. This demonstrates the fixture contract and preservation of its test, not agent adherence to the new workflow. No actual application test, required hook, commit, or test expectation was bypassed or rewritten.

## Context-aware correction — November 9, 2026

The current workflow classifies behavior-preserving refactors, bug fixes, intentional contract changes, and new functionality. It preserves valid behavior tests, permits justified expectation/setup changes, and calls for proportional new coverage, including integration tests for relevant cross-boundary flows. Relevant test work can be part of authorized implementation; explicit narrower user restrictions still apply. A missing suite is assessed by risk and tooling rather than treated as a universal reason to forbid or require tests. Producing a green result by hiding a regression remains inappropriate.

The supplementary manifest now has seven cases. The intentional-contract case permits justified test updates, and two additional cases cover new-feature integration and a bug encoded by an outdated assertion. The no-suite case retains an explicit scenario-specific restriction; it is not a default prohibition. Original specification cases, executable checks, and the refactor's existing test file remain unchanged. Independent behavioral evaluation of these instructions is still pending.

| Executed correction check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 16 documents, 51 local links, original 12 cases valid; exit 0 |
| `node tests/check-fixtures.mjs` | Original executable checks passed unchanged; exit 0 |
| Supplementary manifest and local-anchor inspection through Python/stdin | Seven unique cases with complete criteria and valid inputs; renamed context-aware workflow anchors resolve |
| Behavior-preserving refactor experiment | Baseline/candidate/corrected source exits 0/1/0 with identical existing-test SHA-256 |
| Intended-contract experiment in a separate temporary project | Old contract/old tests passed; requested new default/old expectations failed; new default/justified new expectations passed (exits 0/1/0). Zero and explicit-discount assertions retained; repository fixtures untouched |
| `git diff --check` | No whitespace errors in tracked changes |

The intended-contract experiment changed only the temporary source default from 10% to 0% and the corresponding null/undefined expectations from 90 to 100, as specified by the fixture's business requirement. It illustrates why legitimate test updates differ from concealing regressions. Neither experiment executes the skill through a model or proves integration coverage in an actual frontend application.

## Frontend change safety and rigorous tests — November 9, 2026

The public [retro skill](https://skillrepo.dev/skills/mattpocock/retro) and its [upstream source](https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md) were read as design evidence, not invoked as instructions. Its emphasis on inspecting existing checks and improving demonstrated failure prevention informed this update. FrontScope does not adopt a dependency on `writing-for-agents`, assume reviewer context is sufficient without investigation, or automatically impose hooks/CI on every repository. No session logs, global instructions, or third-party skill installation were required.

New guidance covers scoped frontend edits, preservation of unrelated styling and focus behavior, shared token/component consumers, actual library/version/API research, and review of concrete generated-code defects. Test guidance now separates business/accessibility criticality from finding severity, requires independent behavioral expectations, treats strictness separately from implementation brittleness, and supports minimal useful setup when tests are requested in an application without them. Contextual test changes remain permitted within authorized scope.

Five cases were added to the supplementary manifest: style preservation, versioned library evidence, meaningful assertions, risk-prioritized coverage, and testing setup without a suite. There are now 12 original specification cases plus 12 supplementary cases. The existing validator was extended to validate both manifests automatically instead of leaving supplementary inputs unwired; original scenarios and executable fixture checks were not weakened.

| Executed check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 17 documents, 54 local links, 24 cases across two manifests; both manifests and original T01–T12 mappings valid; exit 0 |
| `node tests/check-fixtures.mjs` | Original regression and clean-control checks passed unchanged; exit 0 |
| Isolated validator experiments via Python/stdin | Intact manifests accepted; seven invalid conditions rejected: missing fixture, out-of-scope path, empty criteria, cross-manifest duplicate ID, malformed JSON, missing supplementary manifest, and missing original T12 mapping |
| Independent-oracle experiment via Node/stdin | Tautological assertion accepted the known shipping boundary defect; contract-derived below/at/above-threshold expectations rejected it and accepted the corrected implementation |
| `python -X utf8 tests/probe_codex.py` | Current package found enabled with `repo` scope; exit 0; no model turn |
| Local-section/whitespace and baseline-resource inspection | Referenced local anchors resolve; Markdown has no trailing whitespace; original `cases.json` and `check-fixtures.mjs` remain unchanged |
| `git diff --check` | No whitespace errors in tracked changes |

The oracle experiment used the supplied business rule (free shipping at subtotal at least 50) and cases 49.99→5, 50→0, and 50.01→0. It evaluated isolated functions without editing repository fixtures or a production application. It does not establish model adherence, visual correctness, library runtime compatibility, or complete coverage. Both manifests still need independent host evaluation.

## Project-organization workflow — November 9, 2026

The existing `structure` mode now covers new-project/feature organization and scoped migrations. The architecture reference defines how to honor a user-selected separation convention, place meaningful hooks/composables, pure functions, grouped constants, and types/interfaces, reuse existing clients/contracts, and report old-to-new paths. It preserves contextual keep/local/shared decisions rather than requiring empty categories or a framework-specific scaffold everywhere. No extra skill installation or runtime was introduced.

Two supplementary cases were added: a chosen React/TypeScript local feature layout, and a planning-only Vue checkout migration preserving public exports, instance lifecycle, existing domain/client ownership, user styling work, and behavioral test contracts. There are now 12 specification cases and 14 supplementary cases; both manifests remain unexecuted as independent model evaluations.

| Executed check | Observed result |
| --- | --- |
| `python -X utf8 tests/validate.py` | 17 documents, 56 local links, 26 cases in two valid manifests; original T01–T12 mappings retained; exit 0 |
| `node tests/check-fixtures.mjs` | Original regression/control checks passed unchanged; exit 0 |
| `python -X utf8 tests/probe_codex.py` | Updated entry point found enabled with `repo` scope; exit 0; no model turn |
| Local anchor/whitespace and original-resource inspection | Referenced sections resolve, Markdown has no trailing whitespace, original cases/executable checks unchanged |
| `git diff --check` | No whitespace errors in tracked changes |

The new fixtures are supplied-context evaluations, not actual generated applications or completed file moves. No frontend project was scaffolded, reorganized, built, or visually validated during these checks.

## What these checks do not establish

- The 12 current cases have inputs and rubrics, but have not been run as an independent model evaluation suite in fresh sessions. The original eight cases remain represented. Three guided reports in [examples.md](examples.md) demonstrate regression, clean control, and fallback; they are not blind evaluations.
- The fourteen supplementary contextual frontend/testing/organization cases are likewise unexecuted as independent model evaluations. Instructions are workflow guidance, not a Git hook or technical guarantee that every host or external commit obeys them.
- No integrated review in a fresh Codex/VS Code session, automatic selection test, or Copilot/Claude Code discovery/execution was performed. End-to-end compatibility remains unverified.
- React/Vue are decision-evaluation code fixtures; components were not mounted in a framework. Angular/Svelte have references without dedicated execution.
- Browser execution, screenshots, visual comparison, profiling, and security/dependency scans were not performed. There is no approved baseline or complete accessibility result.
- `skills-ref` was not run. The local validator is restricted to this package's YAML profile. The skill-creator `quick_validate.py` was not run because PyYAML was missing (`importlib.util.find_spec('yaml')` returned false); nothing was installed for this optional tool.
- JavaScript fixture checks are not an application test suite or proof of correct repository reviews.

Follow the [evaluation procedure](README.md) to run cases in actual agents with identical inputs and separate rubrics.
