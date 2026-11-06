# Supplied evidence for offline analysis

**All packages, versions, and release notes below are fictional.** Do not search for these packages online or install them. JavaScript project; no access to `node_modules`, a terminal, or the network. Pre-upgrade: declared source 1.4.0, proposed target 2.0.0.

Relevant `package.json`:

```json
{
  "dependencies": {
    "@frontscope-fixture/catalog-client": "^1.4.0",
    "@frontscope-fixture/runtime": "2.8.0"
  }
}
```

Excerpt from `package-lock.json`, lockfileVersion 3:

```json
{
  "packages": {
    "node_modules/@frontscope-fixture/catalog-client": { "version": "1.4.2" },
    "node_modules/@frontscope-fixture/runtime": { "version": "2.8.0" }
  }
}
```

Supplied catalog-client 2.0.0 release notes: `listProducts()` remains asynchronous, but its result changes from `Product[]` to `{ items: Product[], nextCursor: string | null }`. The `@frontscope-fixture/runtime` peer changes from `^2.0.0` to `^3.0.0`. No other change is documented in this material. The runtime 3 API was not supplied.

`features/catalog/loadNames.js`:

```js
import { listProducts } from '@frontscope-fixture/catalog-client';
export async function loadNames() {
  const products = await listProducts();
  return products.map(product => product.name);
}
```

The `CatalogPage` caller displays the returned names and uses this function directly without adapting the response. No tests, build, or installation were executed or supplied.
