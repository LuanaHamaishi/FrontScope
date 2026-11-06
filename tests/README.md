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

`validate.py` checks the package's restricted YAML profile (strings and metadata), naming/directory, relative links, resource isolation, manifest integrity, and mappings to specification scenarios T01–T12. Coverage means fixtures and criteria are associated with a scenario, not that behavior passed. It is not a general YAML parser or complete official validator. `check-fixtures.mjs` establishes the sample regression trigger and clean-change equivalence for selected inputs. Success means **the fixture defect was reproduced**, not that the candidate is correct.

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

[examples.md](examples.md) contains demonstrations produced during implementation, not independent evaluations or proof of integrated host execution. Actual check records are in [validation.md](validation.md).

## Next evaluations with sample repositories

- Small React and Vue apps with lockfiles and existing installed suites: locality cases followed by a real diff with a caller/regression test. Use test copies without private data.
- A workspace with a shared library: `impact/deep` on a contract between two packages; verify investigation stays with connected consumers.
- A real dependency upgrade in a test branch: official notes for exact versions, peers, build, and runtime flow. Compare pre-upgrade and post-upgrade analysis.
- A synthetic UI with an existing browser suite: console, focus, viewports, intentional differences, baseline protection, and fallback when browser execution fails.

Angular/Svelte, large monorepos, images, and modification authorization need dedicated evaluations before claiming those behaviors verified. References provide guidance, not integration certification.
