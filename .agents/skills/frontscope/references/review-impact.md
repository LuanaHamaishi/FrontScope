# Review, impact, and investigation

## Review

Confirm the review target: working tree, staged changes, commits, or a PR and its base. When Git is available, read operations such as status, diff, and file inspection help; do not implicitly fetch, check out, or reset. For PRs, distinguish a tip-to-tip diff from the diff since the common ancestor. If the base is missing, request it or limit review to supplied material.

Read the diff and surrounding context. Follow types, callers, consumers, and tests that could confirm or refute a suspicion. Distinguish introduced defects, preexisting problems, and newly exposed older problems; do not attribute an unchanged defect to the PR without demonstrating the relationship.

For each candidate finding, establish:

- Trigger and concrete input; before/after outcome and expected contract.
- Evidence of reachability: caller, configuration, UI flow, or test.
- Causal explanation and impact on users/consumers.
- A possible counterexample: existing guard, earlier validation, different contract, or unreachable code.

Examine empty states, zero, false, null, errors, loading, concurrency, cancellation, and unmounting when relevant. Check types/serialization, events, API compatibility, and effective authorization without applying irrelevant checklists. Reference current file lines or explicitly identify the side of the diff. Without trustworthy numbering, use a symbol/snippet and scope; do not invent line numbers.

A plausible problem with an unproven premise is a potential risk. A preference without a concrete cost is an optional suggestion. A clean diff can produce zero findings.

## Impact

Build a small map: change → contract → consumers → behavior → validation. Include public exports, downstream packages, routes, persistence, state, and integrations only where there is a dependency. Distinguish demonstrated direct impact from inferred indirect impact. Treat unknown external consumers of public APIs as a gap; a local search does not exclude them.

Choose regression checks that distinguish before/after: boundary inputs, errors, normal flow, and relevant integration. State the coverage limits of the investigation.

## Debug

Record expected/observed behavior, environment/versions, and minimal reproduction steps. Separate hypotheses by evidence and choose an observation that can distinguish them. Seek the cause, not just the location of a symptom. Do not declare a definitive cause from correlation. Without reproduction, provide a static diagnosis and next experiment. Do not claim a fix resolved the problem without corresponding validation.
