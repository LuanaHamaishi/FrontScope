# Browser and visual validation: host adapter

This is a v0.1 instruction protocol, not a driver implementation. The host may provide browser automation, a terminal with an existing suite, supplied screenshots, or none of these. Playwright is optional; a manifest dependency does not prove an installed browser, available server, or execution permission.

## Detection and selection

Before acting, record capabilities as **available**, **unavailable**, or **unknown**, with evidence. Assess navigation/interaction, capture, image reading, comparison, console/runtime, test server, and local artifact storage separately. Also verify permissions, target/environment, and data involved.

| Observed condition | Adapter and permitted outcome |
| --- | --- |
| Browser tool plus authorized environment | Use actual host operations; record steps and outcomes |
| Terminal plus existing executable, authorized suite | Inspect configuration/scripts and run the relevant target; do not implicitly install browsers/packages |
| Only supplied screenshots and image reading | Compare visible evidence; do not claim interaction, console inspection, or measurements not supplied |
| No browser/images, or missing authorization | Perform scoped static analysis and provide a manual plan labeled **not executed** |

If a tool fails or the environment does not start, record the error, stop dependent actions, and use the fallback. Do not silently retry installations or expand permissions. Code review does not require a browser.

## Adapter contract

Map logical operations to actual capabilities without inventing APIs: prepare state → open target → configure viewport → interact → observe/capture → inspect console → compare → report. Unsupported operations must be reported as not performed, with a reason. Do not force a single driver or claim future automation is ready.

Minimum inputs: authorized local/test target, case/state, base/candidate revisions when comparing, viewport, and baseline evidence. Output: capabilities/permissions, environment, steps, observations, authorized local artifacts, differences, classification, and gaps. Do not publish or transmit artifacts externally without authorization.

## Execution by mode

- `visual-review`: compare equivalent base/candidate states. Connect a difference to style/template/state lines only with evidence. Distinguish intentional change, possible regression, and inconclusive observations; a visual difference alone is not a confirmed defect.
- `browser-test`: define steps and observable outcome before interaction. Cover requested behavior, available console/runtime errors, and relevant focus/keyboard behavior. Distinguish functionality from appearance.
- `responsive-audit`: derive viewports from relevant breakpoints/devices; check overflow, clipped content, ordering, interaction targets, and focus. Without rendering, describe CSS risks as hypotheses and propose widths to test. Reading media queries does not validate responsiveness.

Control browser version, OS/DPR, viewport, zoom, loaded fonts, locale/timezone, animations, dynamic clock/data, network, and deterministic state. State missing controls and their effect on comparison. Justify pixel tolerances; do not hide differences with broad masks.

Use synthetic data. Obtain authorization before capturing/transmitting sensitive information; prefer states without sensitive data. Never overwrite approved baselines without specific authorization. Updating a baseline does not demonstrate correctness. Without a comparable baseline, report current observations, not a proven regression.

## Usable fallback

Provide the reason for unavailable execution, static observation with file/symbol, test case, proposed environment/viewport, manual steps, expected outcome, and evidence to collect. Example plan: open a synthetic checkout state at widths derived from breakpoints; navigate with Tab; submit a known error; inspect focus, overflow, and message; record console and authorized local screenshots. Label everything not executed. No tool installation is required to deliver this report.
