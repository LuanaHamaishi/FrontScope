# Supplied workspace evidence

JavaScript workspace with `packages/money`, `apps/storefront`, and `apps/admin`. The fictional package names are `@frontscope-fixture/money`, `@frontscope-fixture/storefront`, and `@frontscope-fixture/admin`. Both application manifests declare a direct workspace dependency on `@frontscope-fixture/money`. The version does not change in this diff; no contract change was declared.

Documented money package contract: `formatPrice` accepts nonnegative integer cents and returns a decimal string with two places, without a currency symbol. `1999` must produce `'19.99'`.

Base `packages/money/src/format.mjs`:

```js
export function formatPrice(cents) {
  return (cents / 100).toFixed(2);
}
```

Candidate of the same file:

```js
export function formatPrice(amount) {
  return amount.toFixed(2);
}
```

The public package entry point reexports `formatPrice`. This consumer was inspected: `apps/storefront/src/productPrice.mjs`:

```js
import { formatPrice } from '@frontscope-fixture/money';
export function productPrice(product) {
  return formatPrice(product.priceInCents);
}
```

The catalog product contains `priceInCents: 1999`. A supplied contract test expects `formatPrice(1999)` to return `'19.99'`. No tests were executed in this material.

Code for `apps/admin` and other consumers is unavailable. Its manifest confirms a dependency, not usage of this function, actual inputs, or an affected flow. There is no evidence about external consumers. The evaluation environment permits only reading supplied artifacts; it does not permit fetching, network access, editing, or scanning unavailable workspaces.
