# Vue: conditional reference

Confirm version and Options/Composition API usage. Follow props/emits, refs, computed values, watchers, and lifecycle in the actual code. When suspecting reactivity loss through destructuring, check version/compiler and context: macros can change semantics. Demonstrate the affected flow before reporting it.

A local composable can isolate effects or state for one consumer; pure transformations need not become composables. Distinguish computed derivation from effects in watch/watchEffect and check cleanup. Do not translate React hook dependency rules directly into Vue or recommend global stores for cohesive local state.
