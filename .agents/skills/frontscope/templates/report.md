# FrontScope report contract

Use English by default; honor an explicit request for another language. Fill in only available information; mark inapplicable fields without inventing evidence. Scale the report to the task while preserving these distinctions.

## Executive summary

Mode, depth, target/base, and a short conclusion. If there are no actionable problems, state “No actionable findings identified within the inspected scope” without certifying the rest of the project.

## Context and limits

Record confirmed facts and sources, inferred conventions, explicit constraints, unknowns, and capabilities/permissions affecting the work. Distinguish user-supplied evidence from tool observations. Do not include secrets.

For UI/library changes, identify relevant style/component conventions, library versions and documentation/local API evidence, and intended versus preserved behavior. Mark visual validation unavailable when it was not performed.

## Findings

Order by impact; separate **confirmed findings**, **potential risks**, and **optional suggestions**. Categories may be empty. For each actionable item:

| Field | Content |
| --- | --- |
| ID | Unique identifier within the report, such as F-001; preserve it when discussing that finding |
| Title | Concrete problem or identified optional recommendation |
| Classification | Confirmed / potential risk / optional suggestion |
| Severity | Critical / High / Moderate / Suggestion |
| Confidence | High / medium / low, with reasoning and unresolved premises |
| Location | File and verified line, symbol, or scope; side of the diff where necessary |
| Evidence | Snippet/output/contract, trigger, and causal relationship |
| Technical impact | Affected behavior, consumer, and consequences |
| Recommended action | Smallest appropriate fix, alternative, and trade-off where relevant |
| Validation | Observable case confirming the fix or refuting the risk |

Severity and confidence are separate dimensions:

- **Critical**: demonstrated severe security, data, or functionality risk. Do not use for an undemonstrated hypothesis.
- **High**: significant defect, likely regression, or broken contract.
- **Moderate**: meaningful maintenance, reliability, or performance cost with an explained mechanism.
- **Suggestion**: optional improvement or contextual preference; do not present it as a defect.

Do not promote preferences to Moderate. A risk can have high impact and low confidence: expose its unresolved premise. Do not duplicate the same cause across findings to inflate a report.

## Suggested plan, when applicable

Order the smallest steps needed to address findings, indicating dependencies, scope, risks, and corresponding validation. For responsibility analysis, consider keeping the current implementation as an alternative. A plan does not authorize execution; distinguish recommendations from completed actions. Omit the plan or mark it inapplicable when no intervention is needed.

## Validations performed

For each check: command/tool or inspection, scope/environment, observed result, and output/completion evidence. Classify execution as passed, failed, or blocked; static inspection is not an executed test. Attribute supplied logs to their source. Do not convert an unexecuted plan into a passing result.

For code modifications, classify the intended change (refactor, fix, behavior change, or new functionality), explain the chosen test levels and preserved/new/updated tests, and record baseline when observed and post-change results. Justify changed expectations through business rules/contracts, including integration coverage where relevant. Distinguish confirmed preexisting failures from introduced regressions and failures of unknown origin. Before an authorized commit, identify results covering the current source/tests and disclose any explicit user direction to proceed despite failed or unexecuted checks.

Where testing is part of the task, give a short map of flow/contract → High/Medium/Low test priority and reason → existing/new test and level → observed result or remaining gap. Priorities are separate from finding severity. Identify the independent expected behavior and whether known invalid behavior is actually detected; do not claim this was demonstrated without execution. Record intermittent failed attempts alongside later success.

## Validations not performed

Check, reason (capability, permission, artifact, or scope), consequence, and next step. For visual modes, include capabilities/environment, baseline, and missing controls.

Distinguish no suite, blocked execution, and missing direct coverage. Explain whether adding coverage was justified, implemented within scope, proposed, or deferred, and why. Do not present a proposed test or static inspection as an executed passing test.

## Changes and residual risks

After authorized execution: changed files/contracts, purpose, preserved or intentionally changed behavior, and corresponding checks. Always include uncertainty and uncovered risks; scope any statement that no additional risk was identified. Recommended next steps are not completed actions.

For styling/shared-library changes, explain their necessity and affected consumers; distinguish intentionally changed presentation from unrelated styles kept intact. A check or CI/hook recommendation is not an implemented guardrail unless the wiring and execution were verified.

For project organization, state the selected convention and scope, target tree, responsibility/module rationale, keep/local/shared decisions, and old-to-new paths for an existing project. Distinguish suggestions from completed moves; record import/export, state/lifecycle, style, and test implications without claiming unobserved validation.
