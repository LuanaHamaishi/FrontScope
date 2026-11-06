# React: conditional reference

Confirm version, runtime/SSR, and project conventions. Follow state ownership, props, element/key identity, and effect contracts. For suspected stale closures, races, or missing dependencies, show the render/effect sequence producing the error and existing guards. Check cleanup/cancellation; do not assume every duplicate development execution also happens in production.

A local hook can isolate an effect or coordinate state for one consumer. Pure functions need not become hooks. Do not prescribe Context, memo, useMemo, or useCallback without a concrete boundary/benefit. An isolated re-render does not prove a bottleneck; check evidence and version before recommending optimizations or APIs.
