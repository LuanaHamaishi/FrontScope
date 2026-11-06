# Svelte: conditional reference

Confirm version, reactivity mode (legacy or runes), compilation scope, and SSR where relevant. Follow props, derived state, effects, and events according to that mode; assignment semantics and APIs vary. Check cleanup and differences between server and browser initialization before concluding there is a defect.

Local modules can isolate calculation or integration for one consumer. Do not inadvertently promote instance state to shared module state, especially with SSR. Do not recommend React memoization/hooks or automatic migration between reactivity modes.
