# Skill evaluation

There are two layers: artifact integrity and agent behavior. Structural checks do not establish engineering judgment quality. Fixtures have fixed inputs; model responses vary and are not deterministic tests.

English is the default language for prompts, rubrics, and expected reports. For each case without an explicit language override, assess whether the report is in English. To evaluate localization separately, repeat a case in a fresh session with “Respond in Brazilian Portuguese” or another explicit language request; verify that evidence, severity, and permission boundaries remain unchanged. This is an evaluation procedure, not a claim of completed language testing.

## Reproducible local checks

From the repository root:

```powershell
python -X utf8 tests/validate.py
node tests/check-fixtures.mjs
python -X utf8 tests/probe_codex.py
git diff --check
```

Python 3.9+ is needed only for the validators, and Node with `.mjs` support only for the executable JavaScript fixtures. Neither is required by the skill to review code. The optional probe requires an installed Codex binary, uses existing configuration, and starts/stops one local app-server without a model turn. Host policy may block it. It does not test Copilot, Claude, automatic selection, or review execution.

`validate.py` checks the package's restricted YAML profile (strings and metadata), naming/directory, relative links, resource isolation, both evaluation manifests, and original mappings to specification scenarios T01–T12. It rejects missing manifests, duplicate IDs across manifests, empty/invalid prompts or criteria, and nonexistent/out-of-scope input paths. Coverage means fixtures/criteria are present, not that behavior passed. It is not a general YAML parser or complete official validator. `check-fixtures.mjs` establishes the sample regression trigger and clean-change equivalence for selected inputs. Success means **the fixture defect was reproduced**, not that the candidate is correct.

Optional external validator: `skills-ref validate .agents/skills/frontscope`, as described in the [official specification](https://agentskills.io/specification). Run it only if already available or installation is authorized. The skill-creator `quick_validate.py` requires PyYAML; missing PyYAML does not require installing packages to use FrontScope.

## Behavioral evaluation

The [manifest](cases.json) contains prompts, inputs, and rubrics. Keep answer criteria out of the evaluated agent's context:

1. Start a fresh session in the target agent with the skill installed. Record host/version, model, date, permissions, and capabilities. Verify discovery separately.
2. Supply the `prompt` for **one** case and only its `inputs`, plus the skill. Do not supply `accept`/`reject`, `spec_tests`, output examples, or previous results. Restrict tools according to the fixture. Use an isolated test copy when necessary and keep rubrics outside its workspace. Before execution, record file inventory/content hashes for the reviewed sources and Git status/diff where available; store evidence outside the evaluated source files.
3. Save the report, tool activity, and observed changes in an authorized location. Execution logs count only if generated in that evaluation. Compare only the specified base/candidate.
4. Assess **every** `accept`/`reject` criterion: met, not met, or inconclusive, with supporting excerpts. An observed rejection fails the case; missing evidence does not permit presumed success.
5. Check for unauthorized writing, installations, or external access. Compare before/after inventory and hashes to detect changed, created, or removed source files; inspect tool activity for writes even if later reverted. Exclude only previously authorized evaluation artifacts. T10 requires evidence of read-only behavior: a prompt saying “do not edit” does not establish compliance. For agent/model comparisons, repeat inputs in fresh sessions and record variation. One response is not a guarantee.

Explicit discovery/invocation and automatic selection are separate evaluations. For automatic selection, describe intent without naming the skill and observe whether the host loads the entry point and only relevant references.

| Specification §14 scenario | Case / verification |
| --- | --- |
| T01 — Cohesive component without unnecessary extraction | `local-react` |
| T02 — Mixed responsibilities with local boundaries | `mixed` |
| T03 — Existing hook with one consumer | `single-consumer-hook` |
| T04 — Clean diff without invented findings | `clean` |
| T05 — Meaningful regression and evidence-backed report | `regression` |
| T06 — Upgrade notes correlated with API usage in the fixture | `upgrade` |
| T07 — Unavailable browser with honest fallback | `browser-unavailable` |
| T08 — Comparable React and Vue principles | `local-react` and `local-vue` |
| T09 — Confirmed versus potential monorepo impact | `monorepo-impact` |
| T10 — Explicit review request without writes | `regression`, `clean`, `injection`; compare sources/activity before and after |
| T11 — Unsafe legacy precedent does not become mandatory | `bad-precedent` |
| T12 — Sensitive material without unauthorized capture/sharing | `sensitive-material` |

The manifest has 12 cases, without a one-to-one mapping to the 12 specification scenarios. T08 compares two cases, T10 is cross-cutting, and `injection` adds protection against embedded instructions. Reports with findings need unique IDs; an ordered plan is required when intervention makes sense, without inventing actions for a clean diff.

The `spec_tests` fields make mappings inspectable without copying the external specification into the package. New fixtures use only synthetic code/data; the sensitive-material case does not authorize reading real credentials, capture, or network access. Do not reproduce marked private values or use real enterprise material in evaluation records.

## Context-aware test validation cases

The separate [test-validation manifest](test-validation-cases.json) has fourteen contextual frontend/testing cases. They supplement the original 12 specification cases without changing their inputs, expectations, or T01–T12 mappings. Test decisions depend on intended behavior and project context, not a blanket ban on creating or updating tests. Cases also cover style preservation, actual library evidence, test rigor/priority, first test setup, and project organization.

| Case | Expected decision |
| --- | --- |
| `preserve-existing-tests` | Run existing tests, correct an introduced source regression, and retain original test bytes/expectations |
| `no-suite-with-explicit-test-restriction` | Honor a specific request not to create tests in this case, without generalizing that restriction to other projects |
| `existing-suite-and-stale-result` | Use the package suite despite missing direct coverage; do not reuse a passing result after relevant source changes |
| `blocked-suite-is-not-absent` | Distinguish unavailable tooling from absent tests, functional failure, or passing validation |
| `intentional-contract-conflict` | Justify relevant expectation changes for the requested new contract within ordinary authorized implementation scope |
| `new-feature-integration-coverage` | Plan integration coverage for new form/API/list behavior using the project's existing conventions |
| `bug-fix-updates-outdated-test` | Correct an old assertion encoding the reported bug while preserving unrelated business behavior |
| `preserve-unrelated-styling` | Use an existing error state without rewriting global input styles or removing focus indication |
| `research-versioned-library-contract` | Select the existing wrapper and applicable versioned API; expose unknown installation/documentation evidence |
| `independent-assertions-detect-defects` | Detect a tautological green test and derive meaningful boundary assertions from a business rule |
| `prioritize-critical-test-flows` | Prioritize critical business/accessibility flows while separating test priority from finding severity |
| `bootstrap-useful-tests-without-suite` | Plan minimal compatible test setup and useful integration assertions for an explicit testing request |
| `new-project-local-organization` | Honor a chosen local separation convention for meaningful responsibilities without speculative scaffolding or duplicated types/clients |
| `existing-feature-scoped-organization` | Plan Vue feature moves while preserving public contracts, instance lifecycle, user styling work, and behavioral tests |

Use the same independent-evaluation procedure above. Cases have different scopes: some authorize edits, others only analysis, and some explicitly restrict test edits. Respect each scope; do not generalize its restrictions into universal policy. T10 remains read-only, while normal implementation can include justified test work. For the executable refactor case, prepare the isolated layout described by `fixtures/existing-tests/context.md` before starting the agent. Record test hashes before/after for that case's explicit preservation requirement. For authorized behavior/test changes, inspect the rationale and retained coverage instead of demanding identical test bytes. Never let evaluation setup authorize unrelated changes to FrontScope's real fixtures.

`tests/fixtures/existing-tests/total.test.mjs` is a synthetic project's existing suite for the refactor evaluation, not a replacement for FrontScope's checks. A passing baseline, failing candidate, and passing corrected implementation with unchanged test bytes establish that behavior-preserving contract; they do not prove agent compliance or imply all test changes are inappropriate. The other scenarios deliberately exercise legitimate new coverage and changed expectations. Keep source/test diffs, rationale, tool activity, and observed results for independent evaluation.

The packaging validator now checks both manifests. This removes the previous gap where supplementary inputs required a separate manual integrity check. It still does not grade responses or inspect an agent's actions: do not describe behavioral cases as passed merely because files exist or a synthetic suite ran. Keep test requirements strict about observable contracts but resilient to valid implementation changes; do not equate rigor with brittle assertions about incidental structure.

[examples.md](examples.md) contains demonstrations produced during implementation, not independent evaluations or proof of integrated host execution. Actual check records are in [validation.md](validation.md).

## Next evaluations with sample repositories

- Small React and Vue apps with lockfiles and existing installed suites: locality cases followed by a real diff with a caller/regression test. Use test copies without private data.
- A workspace with a shared library: `impact/deep` on a contract between two packages; verify investigation stays with connected consumers.
- A real dependency upgrade in a test branch: official notes for exact versions, peers, build, and runtime flow. Compare pre-upgrade and post-upgrade analysis.
- A synthetic UI with an existing browser suite: console, focus, viewports, intentional differences, baseline protection, and fallback when browser execution fails.

Angular/Svelte, large monorepos, images, and modification authorization need dedicated evaluations before claiming those behaviors verified. References provide guidance, not integration certification.
