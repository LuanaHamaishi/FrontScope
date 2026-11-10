# Performance, reliability, security, and accessibility

## Optimize

Start with the symptom, flow, data volume, and budget where available. Separate measured profiles from static hypotheses. Assess rendering/reactivity, recomputation, component trees, network waterfalls, bundle size, loading, caching, and resource cleanup. For each hypothesis, identify its mechanism and a measurement: host/framework profiler, trace, waterfall, or bundle analysis **if available**.

Memoization costs comparison, memory, and invalidation; caches can serve incorrect data and need bounds. Justify recommendations through a concrete computation/identity/flow and measure before/after when authorized. Render count alone is not a defect without impact. Without instruments, propose an experiment, not improvement percentages.

## Test

Map risk → behavior → test level → observable assertion. Use unit tests for isolated rules, integration tests for contracts/effects, component tests for semantic interaction, and E2E tests for critical journeys. Consider relevant errors, empty states, concurrency, cancellation, and data boundaries. Prioritize reproducible regression protection, not arbitrary coverage targets.

Mocks should honor real contracts and not hide the incompatibility under investigation; avoid mocking the very boundary the test should validate. Improve testability through a local boundary when needed, without creating abstractions merely to satisfy mocks. Inspect existing infrastructure and commands before suggesting new tools.

Only mark a check as passed after observing command, scope, output, and completion. Distinguish passed, failed, blocked, and not performed. Attribute user-supplied results to the user; a proposed command is not execution.

## Test criticality and evidence

Prioritize behavior by user/business impact, likelihood of failure, affected consumers, recovery cost, and current protection. State the reasoning; do not derive criticality solely from lines changed or a coverage percentage. Test priority is not finding severity: an important untested flow is not automatically a demonstrated Critical defect.

| Test priority | Typical context, to confirm in the project | Protection to consider |
| --- | --- | --- |
| High | Authorization boundaries, sensitive data, irreversible actions, money/data correctness, duplicate submissions, or a blocked critical accessible journey | Contract/regression tests plus meaningful integration or critical user-flow checks; include failures and boundary states |
| Medium | Recoverable feature behavior, filtering/pagination, adapters, and state synchronization with limited blast radius | Focused unit/component/integration tests at the relevant boundary |
| Low | Limited presentation or simple low-impact transformations with easy recovery | Existing checks or a small focused test when valuable; explain any deferred new coverage |

Examples are not fixed classifications. A style change hiding focus or an error state can be high priority; a small shared helper can affect many critical consumers. Unknown business impact should remain unknown with the evidence needed to resolve it. Report the critical flows inspected, selected tests, and unprotected cases rather than inventing a numerical risk score.

Strong tests have an independent oracle: a business rule, public contract, user-visible outcome, or trusted example. Assert meaningful values, states, errors, and side effects. A test that computes its expected value using the same faulty logic, compares a function with itself, or checks only that a mock was invoked can pass while behavior is wrong. For integration, retain the real collaborating components/modules and mock only an appropriate external boundary; verify the resulting behavior, not just plumbing.

Where useful and authorized, demonstrate that a test distinguishes correct behavior from a known regression or plausible broken input in an isolated example. Do not mutate production code or start a mutation-testing platform automatically. Treat this demonstration as fixture/test evidence, not proof of complete correctness. Prefer resilient behavioral assertions over incidental DOM structure, call counts, internal state, or broad snapshots unless those details are the actual contract. Strict expectations should detect errors without becoming brittle to valid implementation changes.

If a failure appears intermittent, retain evidence of failed and passing attempts and investigate state, timing, environment, or the underlying defect. Do not rerun until green and report only the successful attempt, delete flaky coverage, or raise tolerances to conceal meaningful changes. Separate demonstrated preexisting failures from unknown causes.

### Projects without tests

When testing setup or coverage is requested, inspect the real framework, language, build system, dependency versions, scripts, and team conventions. Within the existing authorization, implement the smallest useful setup and behavior tests rather than stopping at “no tests found.” Reuse available compatible tooling; preserve scripts/build settings and avoid multiple overlapping runners. Explain required dev dependencies or infrastructure, and respect permissions for installation or external access. If execution is blocked, deliver what is possible and record the blocker instead of fabricating results.

Start with the most important reachable contract or user flow, including an error/boundary case; choose unit, component, integration, or E2E according to what must collaborate. Do not insist that a new suite cover the whole application or make every low-risk change create a test. An explicit no-test-edit restriction remains specific to that request, not a universal policy.

## Context-aware test validation

Apply this workflow to authorized code modifications in any mode, not only `test`, and to separately authorized commits. Recommendations and read-only reviews do not authorize edits or commits. Documentation-only work needs appropriate document checks rather than an unrelated application test suite.

1. **Discover the project's testing context.** Inspect manifests, test files, configuration, documented commands, and CI requirements in the affected package and relevant consumers. Identify existing test levels, fixtures/mocks, architecture, and user restrictions. Use the project's actual runner/package manager. Missing direct coverage is not absence of a suite, and existing tests are evidence rather than an infallible business specification.
2. **Classify the intended behavior.** Compare the request, business rules, public contracts, consumers, and tests before deciding what should change. Separate behavior-preserving refactoring, bug fixing, intentional behavior changes, and new functionality. If intent is ambiguous, investigate or clarify that uncertainty rather than choosing whichever code or test is easier to change. Establish an observed baseline when feasible; otherwise do not label failures preexisting.
3. **Choose meaningful coverage.** Preserve, update, or add tests according to the decision table below. Derive expected outcomes from the intended contract, not from whatever the implementation happens to return. Prefer the project's existing structure and tooling. Test important success, error, and boundary behavior. For new or changed interactions across modules, UI/data flows, or API boundaries, include appropriate integration coverage rather than relying only on isolated mocks; use component/E2E tests where they cover the relevant user journey. Small low-risk changes do not automatically require a new test file or a framework.
4. **Implement code and justified test changes within scope.** A normal request to implement a feature, fix, or refactor can include the relevant test work needed to complete it; do not demand separate approval for each test edit when already authorized by that scope. Respect explicit read-only or no-test-edit restrictions. Explain changed expectations, fixtures, snapshots, imports, mocks, or configuration and their relationship to the intended behavior. Snapshot updates require checking the actual differences, not blind acceptance. Preserve unrelated coverage and the user's existing work.
5. **Run and diagnose.** After each completed code change or coherent step, run relevant existing tests plus new/updated tests. Without direct coverage, run the applicable package/project suite. Follow required checks; broaden when scope or failures justify it rather than scanning the full monorepo after each keystroke. On failure, establish whether the cause is an implementation regression, an outdated/incorrect test, a legitimate new contract, a preexisting defect, or the environment. Correct the responsible code or test with evidence. Do not weaken assertions, skip/exclude failures, lower thresholds, or bypass hooks merely to manufacture a passing result.
6. **Handle absent suites and blocked execution proportionally.** If no tests exist, assess whether useful coverage is justified by behavior, risk, project structure, and authorized scope; absence alone neither mandates a test platform nor rules out writing a meaningful test. Use suitable available tooling or propose the minimum necessary setup. Package installation, external services, and other actions outside existing authorization still need corresponding permission. If tests cannot run, report them as blocked/not performed, not absent or passed. Use relevant static checks without calling them test execution and disclose any residual coverage gap.
7. **Check again before an authorized commit.** Ensure results cover the exact current source, test inputs, and required scope. Rerun affected checks after relevant edits; reuse observed passing results when nothing relevant changed. Review both implementation and test diffs for justified behavior and retained protections. Do not commit through failed or unexecuted required checks unless the user explicitly directs proceeding after disclosure. A missing suite is a limitation to assess, not automatic failure. Never commit automatically or bypass hooks to hide failures.

| Change | Appropriate test decision |
| --- | --- |
| Behavior-preserving refactor | Preserve observable expectations; adapt test setup/imports if structure changed legitimately, avoiding needless coupling to internals |
| Bug fix | Add or update regression protection for the intended correct behavior; an old assertion encoding the bug may need correction with an explained rationale |
| Intentional behavior/contract change | Update affected expectations and add boundary/integration coverage as needed; demonstrate the intended new contract while retaining unrelated behavior |
| New functionality | Add meaningful tests proportional to risk and project conventions, including integration coverage for new cross-boundary flows |

Record behavior classification, selected coverage and rationale, existing/new/updated tests, baseline when observed, actual commands/results, preexisting failures, and unexecuted checks. Explain why each changed test expectation represents the intended behavior and which protections remain. Build, typecheck, lint, and tests are distinct validations. Relevant local tests ordinarily fall within authorized implementation and host permissions; respect narrower restrictions and do not silently expand into installations, external access, sensitive data, or destructive actions.

## Security and accessibility

Follow data into relevant sinks: dynamic HTML, URLs, navigation, cross-origin messages, and storage. Check trust boundaries, context-appropriate escaping/sanitization, sensitive data in bundles/logs/storage, server-side validation, and effective origins. Frontend validation does not establish authorization. For dependencies, use current advisory evidence when available and authorized; lack of a scanner does not establish absence of vulnerabilities.

Inspect semantic HTML, accessible names, labels, order/focus, keyboard behavior, states, error messages, and appropriate ARIA. Native elements can provide interaction without extra scripts. Contrast and layout can require rendering; static analysis does not establish appearance, screen-reader experience, or complete compliance. A lightweight review is not a complete security/accessibility audit.

## Audit and explain

In `audit`, define package, flows, and sample before expanding. Load specialized references only for relevant issues. Prioritize impact and confidence and expose unexamined areas. In `explain`, teach mechanisms and trade-offs with labeled examples; do not turn preferences into requirements.
