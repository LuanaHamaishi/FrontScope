# FrontScope

**Frontend Engineering Intelligence for AI coding agents — v0.1.0**

FrontScope is a portable Agent Skill that helps coding agents understand frontend repositories, review changes, evaluate architectural boundaries, separate responsibilities, and plan safe software evolution.

Its workflows connect recommendations to the repository's actual contracts, conventions, consumers, and constraints. A valid implementation should not be flagged simply because another implementation is preferred.

> Understand before recommending. Justify before modifying. Validate before claiming correctness.

The current implementation is an instruction-based skill with focused references, a report template, reproducible evaluation fixtures, and development checks. The host agent provides tools and executes the workflow. Basic code reviews require no package installation or dedicated runtime.

English is the default language for the skill instructions, documentation, evaluation material, and review reports. You can explicitly request another response language, for example **“Respond in Brazilian Portuguese”**. Technical identifiers and existing application text are preserved unless their translation is authorized.

## What FrontScope provides today

FrontScope v0.1 prioritizes contextual analysis and conservative engineering decisions:

- **Context discovery:** inspect the relevant repository scope, manifests, versions, lockfiles, build configuration, tests, conventions, and architectural constraints before making substantial recommendations.
- **Code and PR review:** investigate changes, contracts, callers, and consumers; distinguish introduced regressions from existing problems and optional preferences.
- **Architecture and impact analysis:** examine module boundaries, dependency direction, coupling, cohesion, workspace relationships, and downstream effects.
- **Responsibility and component design:** decide whether logic should remain in place, move into a local module, or become shared when there is architectural justification.
- **Refactoring advice and authorized implementation:** explain the trade-offs, preserve observable behavior, and prefer the smallest appropriate change within the authorized scope.
- **Dependency migration guidance:** compare declared, resolved, and observable installed versions; connect release notes, breaking changes, affected usage, and peer dependencies to a validation plan.
- **Quality guidance:** investigate performance, testing, reliability, frontend security, accessibility, and debugging with explicit evidence and uncertainty.
- **Browser and visual workflows:** detect available host capabilities and choose browser tools, an existing test suite, supplied screenshots, or a clearly labeled manual fallback.
- **Consistent reporting:** describe findings with unique report IDs, severity, confidence, evidence, impact, recommended action, and validation guidance; include an ordered plan when applicable.

Performance profiling, dependency scanning, browser automation, and image comparison depend on tools supplied by the host. FrontScope does not bundle those engines.

## Engineering principles

### Context before judgment

Investigation starts with the requested file, feature, package, or diff and expands only when needed. FrontScope separates confirmed conventions, inferred patterns, explicit constraints, and unknown information. Existing conventions matter, but they are not automatically proof of correctness.

### Locality first, reusability when needed

Responsibility separation has three valid outcomes:

| Decision | Appropriate when |
| --- | --- |
| Keep the responsibility in the existing component or module | It is cohesive, understandable, and inexpensive to maintain locally. |
| Extract a nearby local module | An independent rule, effect, integration, or testing boundary improves clarity, even with one consumer. |
| Promote it to a shared module | Stable responsibilities, ownership, consumers, and dependency boundaries justify a shared contract. |

Function length alone does not justify extraction. The skill does not automatically create `hooks/`, `services/`, `helpers/`, `context/`, or `shared/` directories, and it does not impose an architectural pattern.

### Evidence before claims

Confirmed defects, potential risks, and optional suggestions are reported separately. Measured bottlenecks remain distinct from optimization hypotheses. Tests, builds, browser interactions, and visual comparisons are only reported as executed when there is observed evidence. Finding no actionable problems is a valid outcome.

## Repository structure

```text
.agents/skills/frontscope/
  SKILL.md
  references/
    context.md
    review-impact.md
    architecture.md
    upgrades.md
    quality.md
    browser.md
    react.md
    vue.md
    angular.md
    svelte.md
  templates/
    report.md
tests/
  cases.json
  fixtures/
  validate.py
  check-fixtures.mjs
  probe_codex.py
  README.md
  examples.md
  validation.md
README.md
```

The distributable package is the entire `.agents/skills/frontscope/` directory. Its `SKILL.md` uses YAML frontmatter and relative resource links following the [Agent Skills specification](https://agentskills.io/specification).

| Resource | Responsibility |
| --- | --- |
| [SKILL.md](.agents/skills/frontscope/SKILL.md) | Entry point, mode selection, investigation depth, permissions, and shared decision rules. |
| [context.md](.agents/skills/frontscope/references/context.md) | Progressive repository discovery and capability-aware investigation. |
| [review-impact.md](.agents/skills/frontscope/references/review-impact.md) | Diff review, consumer analysis, change impact, and debugging. |
| [architecture.md](.agents/skills/frontscope/references/architecture.md) | Architectural boundaries, responsibility placement, and conservative refactoring. |
| [upgrades.md](.agents/skills/frontscope/references/upgrades.md) | Pre-upgrade and post-upgrade compatibility assessment. |
| [quality.md](.agents/skills/frontscope/references/quality.md) | Performance, testing, reliability, security, accessibility, and technical explanation. |
| [browser.md](.agents/skills/frontscope/references/browser.md) | Host capability detection, browser workflows, visual review, and fallbacks. |
| Framework references | Optional guidance for [React](.agents/skills/frontscope/references/react.md), [Vue](.agents/skills/frontscope/references/vue.md), [Angular](.agents/skills/frontscope/references/angular.md), and [Svelte](.agents/skills/frontscope/references/svelte.md). |
| [report.md](.agents/skills/frontscope/templates/report.md) | Shared findings and validation report contract. |
| [tests/](tests/README.md) | Evaluation instructions, fixtures, acceptance criteria, and development checks. |

The entry point routes the agent to relevant references rather than loading every guide for every task. Evaluation files stay outside the distributable package.

## Installation

Copy the complete `frontscope` directory into the discovery location used by your agent. Keep `SKILL.md`, `references/`, and `templates/` together; copying only the entry point leaves its supporting resources unavailable.

The locations below are documented installation targets. They are separate from the verification status of FrontScope itself, described under Compatibility and validation status.

| Agent | Project installation | Explicit invocation | Documentation |
| --- | --- | --- | --- |
| OpenAI Codex | `<project>/.agents/skills/frontscope/` | `$frontscope` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) |
| GitHub Copilot in VS Code | `<project>/.github/skills/frontscope/` | `/frontscope` in a supporting chat session | [VS Code Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) |
| Claude Code | `<project>/.claude/skills/frontscope/` | `/frontscope` | [Claude Code skills](https://code.claude.com/docs/en/skills) |

### Copying into another project

Run this PowerShell example from the FrontScope repository root. Change the project path and discovery directory for your agent. It refuses to overwrite an existing installation.

```powershell
$projectRoot = 'C:\path\to\your-project'
$skillsRoot = Join-Path $projectRoot '.agents\skills'
$destination = Join-Path $skillsRoot 'frontscope'
if (Test-Path -LiteralPath $destination) {
    throw 'An installation already exists. Compare versions before updating.'
}
New-Item -ItemType Directory -Path $skillsRoot -Force | Out-Null
Copy-Item -LiteralPath '.agents\skills\frontscope' -Destination $destination -Recurse
```

For Copilot, use `.github\skills` as the discovery directory. For Claude Code, use `.claude\skills`. Avoid duplicate installations with the same skill name in multiple locations scanned by the same host.

### Using it in VS Code

For the Codex extension, open the target project, start a fresh session, and request `$frontscope` explicitly. In this repository, the package is already in the project-level Codex discovery location.

For Copilot, select the intended agent harness, open **Chat: Open Customizations → Skills**, and inspect the installed skill. In a fresh conversation, look for `/frontscope` in the `/` menu and try a small task. Availability can depend on the installed version and organizational policy.

Verify that the agent loads the expected instructions and resources. Test automatic selection separately using a matching natural-language request without the skill name. Installing or listing a skill does not establish that a host will select or execute it correctly.

## Modes and investigation depth

Users can name a mode or describe their intent naturally. Mode names guide the workflow; FrontScope does not implement a separate command-line parser or executable subcommands.

| Mode | Intended outcome |
| --- | --- |
| `review` | Review code or a PR with findings tied to evidence and affected consumers. |
| `architect` | Evaluate module boundaries, dependencies, cohesion, and architectural consistency. |
| `refactor` | Recommend refactoring or implement a minimal change when explicitly authorized. |
| `structure` | Decide where responsibilities belong and whether extraction should remain local. |
| `upgrade` | Assess dependency compatibility, migration work, and validation needs. |
| `impact` | Trace a change through contracts and consumers. |
| `optimize` | Investigate performance symptoms and distinguish measurements from hypotheses. |
| `test` | Recommend behavior-based regression protection and appropriate test levels. |
| `debug` | Investigate unexpected behavior through reproduction, hypotheses, and evidence. |
| `audit` | Assess engineering concerns within an explicit scope and sample. |
| `explain` | Explain decisions, mechanisms, alternatives, and trade-offs. |
| `visual-review` | Analyze visual differences using available evidence and comparable states. |
| `browser-test` | Validate browser behavior through host tools or provide an unexecuted test plan. |
| `responsive-audit` | Assess responsive behavior across relevant viewports or document static risks and manual checks. |

| Depth | Investigation scope |
| --- | --- |
| `quick` | The target and its immediate contract or consumer; focused, low-cost analysis. |
| `standard` | Default: relevant package context, consumers, and existing tests. |
| `deep` | Broader dependency, architectural, and critical-flow investigation when justified. |

Depth never grants permission to edit files or scan an entire monorepo unnecessarily.

## Usage examples

These are example requests, not claims that the tasks have been executed. Replace paths, branches, package names, and versions with real inputs. The examples use Codex's `$frontscope` prefix; use the corresponding invocation for your agent. Reports default to English; explicitly request another language when needed.

### Review a staged change

```text
$frontscope Review the staged diff in quick mode. Check relevant callers for
behavioral regressions and broken contracts. Do not edit source files.
```

Expected focus: the staged changes and relevant consumers, confirmed findings separated from risks, and an explicit account of checks performed or not performed. A clean diff can produce zero findings.

### Review changes against an explicit base

```text
$frontscope Review the changes from the common ancestor of main and HEAD.
Use standard depth and focus on src/features/checkout. Explain the impact
on callers and existing tests. Do not fetch, change branches, or edit files.
```

Provide the diff and relevant files directly if Git or repository access is unavailable. The agent should identify missing evidence rather than invent a comparison base.

### Evaluate architecture and change impact

```text
$frontscope Use architect and impact modes at deep depth to assess the
dependency boundaries between packages/ui and apps/storefront. Start with
their manifests and public exports, then inspect affected consumers.
Explain concrete coupling costs and trade-offs before proposing changes.
Do not reorganize files.
```

### Decide whether responsibilities should be extracted

```text
$frontscope Use structure/standard to assess
src/features/checkout/CheckoutForm.vue. Decide what should stay in the
component, what could become a nearby local module, and what would justify
a shared abstraction. A single consumer is acceptable. Do not edit files.
```

Expected focus: cohesion, complexity, testability, ownership, and project conventions. Extraction is not required merely because the component contains state or helper functions.

### Implement a refactor within an authorized scope

```text
$frontscope Use refactor/standard. You may extract the tax calculation from
src/features/checkout/Checkout.tsx into a local module beside it and adjust
its existing unit tests. Explain the plan first and preserve observable
behavior. Run the relevant existing local unit tests if they require no
installation or network access. Do not move unrelated files or commit.
```

The skill separates review from execution. Permission to assess a component does not imply permission to modify it; an explicit implementation request defines the authorized scope.

### Assess a dependency migration

```text
$frontscope Use upgrade/standard to assess moving <package> from
<original-version> to <target-version>. Inspect the relevant manifest,
lockfile, usages, wrappers, and peer dependencies. Use the supplied official
release notes and migration guide. Identify affected contracts and propose
a validation plan. Do not install or upgrade anything.
```

For an offline assessment, provide the notes with their provenance and version coverage. Declared ranges, lockfile resolutions, and observed installed versions should remain distinct.

### Investigate a performance symptom

```text
$frontscope Use optimize/standard to investigate slow filtering in
src/features/catalog. Inspect the data flow and rendering behavior.
Separate measured bottlenecks from hypotheses, justify any caching or
memoization proposal, and describe the measurements still needed.
```

### Plan regression protection

```text
$frontscope Use test/standard to assess regression protection for the
checkout submission flow. Inspect existing tests and recommend the smallest
useful combination of unit, integration, component, or end-to-end tests.
Tie each recommendation to behavior and risk. Do not add dependencies.
```

### Debug unexpected behavior

```text
$frontscope Use debug/standard. Search results sometimes show an older query
after a newer query completes. Inspect the request lifecycle and relevant
consumers, distinguish hypotheses from confirmed causes, and propose a
minimal reproduction. Do not edit code yet.
```

### Run a scoped engineering assessment

```text
$frontscope Use audit/standard for src/features/account. Review relevant
reliability, frontend security, and accessibility concerns, including input
handling, browser storage, keyboard navigation, and focus. State the scope
and limits; prioritize evidence-backed findings. Do not modify files.
```

A scoped review does not constitute a complete security or accessibility audit.

### Explain a design decision

```text
$frontscope Use explain mode to compare keeping this logic inside the
component with extracting a local composable or service. Explain the
trade-offs, when each option is appropriate, and when extraction adds no
value. If useful, include a Mermaid diagram labeled as illustrative.
```

### Request visual, browser, and responsive validation

```text
$frontscope Use visual-review, browser-test, and responsive-audit for the
OrderSummary change. Detect the available tools first. Use only the
authorized local test environment with synthetic data; compare equivalent
states and derive viewports from the project's breakpoints.
Do not install tools, transmit screenshots, or overwrite approved baselines.
If execution is unavailable, provide a clearly labeled manual test plan.
```

Expected focus: actual capabilities and permissions, environment consistency, observed behavior, baseline availability, and uncertainty. A visual difference alone is not a confirmed defect.

### Use natural language without naming a mode

```text
$frontscope Does this Vue component actually need a composable, or is its
current local organization appropriate? Follow the project's conventions
and explain the maintenance trade-offs. Do not edit files.
```

Automatic activation can also be tested by omitting `$frontscope` and making a matching request. Observe whether the host actually loads the skill; do not assume selection.

### Request a report in another language

```text
$frontscope Review the staged diff in quick mode without editing files.
Respond in Brazilian Portuguese.
```

This changes the response language for the request while preserving the same engineering workflow, evidence requirements, and permission boundaries.

## Report format

The [shared report contract](.agents/skills/frontscope/templates/report.md) includes an executive summary, context and limits, findings, validations performed, validations not performed, and remaining risks. Authorized changes add the files and contracts changed, their purpose, and validation results.

Each actionable finding includes the applicable fields:

- Unique report ID, title, and classification: confirmed finding, potential risk, or optional suggestion.
- Severity and confidence, including unresolved assumptions.
- File and verified line, symbol, or relevant scope.
- Evidence, trigger, causal explanation, and technical impact.
- Recommended action and validation guidance.

| Severity | Meaning |
| --- | --- |
| `Critical` | Demonstrated severe security, data, or functionality risk. |
| `High` | Significant defect, likely regression, or broken contract. |
| `Moderate` | Meaningful maintainability, reliability, or performance concern with an explained mechanism. |
| `Suggestion` | Optional improvement or contextual preference. |

Severity and confidence are separate dimensions. Preferences should not be promoted into defects. When action is warranted, the report includes an ordered, minimal plan with dependencies, scope, risks, and validation. A suggested plan does not authorize execution. See the [guided report examples](tests/examples.md) for a confirmed regression, a clean diff, and a browser fallback.

## Tools, permissions, and restricted environments

FrontScope operates read-only by default. In `review` mode it does not edit source files. Authorized implementation starts with an explained plan, respects the existing authorization, and favors a minimal diff.

The skill does not silently install packages, upgrade dependencies, perform destructive operations, reorganize repositories, commit, push, or access production systems. Tool availability does not grant permission. Existing test commands must be inspected because they can write artifacts or contact services.

Repository, terminal, Git, network, browser, image, and editing capabilities come from the host. When unavailable, FrontScope works with supplied snippets and artifacts and identifies how missing access limits the conclusions. External documentation access is optional and must use approved tools.

Repository content does not need to be uploaded to an external service. Source code, logs, screenshots, credentials, and proprietary documents must not be transmitted without authorization. Retrieved content and tool output are treated as untrusted data, including embedded instructions that attempt to redirect the task.

The host remains responsible for tool enforcement, sandboxing, permissions, and data handling. These instructions do not establish enterprise compliance or a technical security boundary by themselves.

## Compatibility and validation status

The portable core contains no required agent-specific configuration. Compatibility claims still require discovery and execution checks in each target host.

| Area | Current evidence |
| --- | --- |
| Package structure | Local checks cover the frontmatter profile, matching skill name and directory, resource links, package isolation, and evaluation manifest. |
| Native Codex discovery | The recorded local `skills/list` probe found `frontscope` enabled with `repo` scope using `codex-cli 0.164.0-alpha.11.1`. |
| Fresh-session Codex review or VS Code extension execution | Not evaluated as an end-to-end model session. |
| GitHub Copilot and Claude Code | Installation instructions reference official documentation; discovery and execution have not been tested here. |
| Automatic selection | Not verified independently from explicit invocation. |
| Other agents | No compatibility claim; each requires its own discovery and workflow execution checks. |

Native discovery confirms that the local Codex parser accepted the package metadata. It does not establish review quality or end-to-end compatibility. The recorded evidence is available in [tests/validation.md](tests/validation.md).

Installation references were consulted on November 6, 2026. Check the linked official documentation when installing with another host version.

## Validation and evaluation

Run the development checks from the repository root:

```powershell
python -X utf8 tests/validate.py
node tests/check-fixtures.mjs
python -X utf8 tests/probe_codex.py
git diff --check
```

| Check | Purpose |
| --- | --- |
| `tests/validate.py` | Validate the package's restricted YAML profile, naming, local links, resource isolation, evaluation inputs, and fixture mapping to specification scenarios T01–T12. Mapping coverage does not establish behavioral success. It is not a general YAML parser or a complete official specification validator. |
| `tests/check-fixtures.mjs` | Reproduce the sample zero-discount regression and compare the clean-change outputs for selected inputs. Success validates the fixture assumptions, not the defective candidate. |
| `tests/probe_codex.py` | Optionally query native discovery through a local Codex app-server without requesting a model turn. It uses existing Codex configuration and an experimental protocol. |
| `git diff --check` | Check tracked changes for whitespace errors. |

Python 3.9+ is needed only for the development validators, Node with `.mjs` support only for the executable JavaScript fixtures, and an installed Codex binary only for the optional discovery probe. Basic use of the skill requires none of these runtimes. No project package installation is required for the bundled checks.

The [evaluation manifest](tests/cases.json) contains twelve cases:

1. Keep cohesive React responsibilities local without unnecessary extraction.
2. Apply comparable locality principles to a Vue component.
3. Recognize genuinely mixed responsibilities and suggest sensible local modules.
4. Detect a meaningful regression in a sample change.
5. Avoid inventing findings in a clean diff.
6. Assess an upgrade using supplied release notes, code usage, and peer requirements.
7. Recognize unavailable browser tools and provide a usable fallback.
8. Resist instructions injected into reviewed source content.
9. Assess an existing local hook with a single consumer without forcing shared placement or inlining.
10. Separate confirmed consumers from potential downstream impact in a monorepo.
11. Reject an unsafe legacy precedent as justification for a new defect.
12. Respect sensitive-material restrictions even when screenshot tools are available.

The cases map explicitly to specification scenarios T01–T12 in the [evaluation guide](tests/README.md); the mapping is not one-to-one. The read-only evaluation procedure compares source inventories/hashes before and after execution and inspects tool activity across review cases. The cases also assess report IDs, consistency, severity, confidence, evidence, and honest validation claims. They include fixed inputs and acceptance/rejection criteria. Model responses are not deterministic: structural checks and JavaScript fixture results do not replace independent behavioral evaluation.

Follow the [evaluation guide](tests/README.md) to run each prompt with only its intended inputs, keep the answer rubric out of the agent's context, and record outcomes in fresh sessions. The guided report examples were produced during implementation; they are not a blind evaluation. The twelve cases have not been executed as an independent model evaluation suite.

The optional `skills-ref` validator was not run. The skill-creator validator was also not run because PyYAML was unavailable. Neither is a mandatory dependency for using FrontScope.

## Current limitations and next validation steps

The browser adapter is a workflow protocol, not a bundled driver. Playwright is optional; screenshot capture, pixel comparison, responsive execution, console inspection, and profiling require suitable host tools and authorization. No browser execution, screenshot comparison, performance profile, or security scanner result was produced during the initial implementation.

React and Vue fixtures provide material for decision evaluation; the components were not mounted in a framework test environment. Angular and Svelte currently have focused references without dedicated execution scenarios. Broader monorepo accuracy, permission handling during modifications, and end-to-end behavior still need targeted evaluation.

A successful build does not prove runtime migration compatibility. Static inspection does not establish visual correctness, full accessibility, security completeness, or exhaustive repository coverage.

Recommended next checks are small React and Vue sample repositories, a workspace with a changed shared contract, a real dependency migration in a test branch, and a synthetic UI with an existing browser suite. Detailed suggestions and acceptance procedures are in the [evaluation guide](tests/README.md).
