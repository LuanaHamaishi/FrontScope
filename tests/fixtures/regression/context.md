# Checkout contract

A pure JavaScript function used in the summary and to produce the order amount. `subtotal` is nonnegative and `discountPercent` is validated before invocation: a number from 0 to 100, null, or undefined. Zero means no discount; null/undefined select the default 10% discount. The caller sends `total(100, 0)` for a purchase without a promotion. `before.mjs` is the base and `after.mjs` is the candidate. Editing, installations, and network access are not authorized. If a terminal exists, local checks without network access are authorized.
