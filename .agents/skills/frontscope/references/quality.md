# Performance, reliability, security, and accessibility

## Optimize

Start with the symptom, flow, data volume, and budget where available. Separate measured profiles from static hypotheses. Assess rendering/reactivity, recomputation, component trees, network waterfalls, bundle size, loading, caching, and resource cleanup. For each hypothesis, identify its mechanism and a measurement: host/framework profiler, trace, waterfall, or bundle analysis **if available**.

Memoization costs comparison, memory, and invalidation; caches can serve incorrect data and need bounds. Justify recommendations through a concrete computation/identity/flow and measure before/after when authorized. Render count alone is not a defect without impact. Without instruments, propose an experiment, not improvement percentages.

## Test

Map risk → behavior → test level → observable assertion. Use unit tests for isolated rules, integration tests for contracts/effects, component tests for semantic interaction, and E2E tests for critical journeys. Consider relevant errors, empty states, concurrency, cancellation, and data boundaries. Prioritize reproducible regression protection, not arbitrary coverage targets.

Mocks should honor real contracts and not hide the incompatibility under investigation; avoid mocking the very boundary the test should validate. Improve testability through a local boundary when needed, without creating abstractions merely to satisfy mocks. Inspect existing infrastructure and commands before suggesting new tools.

Only mark a check as passed after observing command, scope, output, and completion. Distinguish passed, failed, blocked, and not performed. Attribute user-supplied results to the user; a proposed command is not execution.

## Security and accessibility

Follow data into relevant sinks: dynamic HTML, URLs, navigation, cross-origin messages, and storage. Check trust boundaries, context-appropriate escaping/sanitization, sensitive data in bundles/logs/storage, server-side validation, and effective origins. Frontend validation does not establish authorization. For dependencies, use current advisory evidence when available and authorized; lack of a scanner does not establish absence of vulnerabilities.

Inspect semantic HTML, accessible names, labels, order/focus, keyboard behavior, states, error messages, and appropriate ARIA. Native elements can provide interaction without extra scripts. Contrast and layout can require rendering; static analysis does not establish appearance, screen-reader experience, or complete compliance. A lightweight review is not a complete security/accessibility audit.

## Audit and explain

In `audit`, define package, flows, and sample before expanding. Load specialized references only for relevant issues. Prioritize impact and confidence and expose unexamined areas. In `explain`, teach mechanisms and trade-offs with labeled examples; do not turn preferences into requirements.
