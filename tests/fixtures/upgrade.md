# Evidências fornecidas para análise offline

**Todos os pacotes, versões e release notes abaixo são fictícios.** Não buscar esses pacotes na internet nem instalá-los. Projeto JavaScript; sem acesso a `node_modules`, terminal ou rede. Pré-upgrade: origem declarada 1.4.0, destino proposto 2.0.0.

`package.json` relevante:

```json
{
  "dependencies": {
    "@frontscope-fixture/catalog-client": "^1.4.0",
    "@frontscope-fixture/runtime": "2.8.0"
  }
}
```

Extrato de `package-lock.json` lockfileVersion 3:

```json
{
  "packages": {
    "node_modules/@frontscope-fixture/catalog-client": { "version": "1.4.2" },
    "node_modules/@frontscope-fixture/runtime": { "version": "2.8.0" }
  }
}
```

Release notes fornecidas de catalog-client 2.0.0: `listProducts()` continua assíncrono, mas seu resultado deixa de ser `Product[]` e passa a `{ items: Product[], nextCursor: string | null }`. O peer `@frontscope-fixture/runtime` passa de `^2.0.0` para `^3.0.0`. Não há outra mudança documentada neste material. API runtime 3 não foi fornecida.

`features/catalog/loadNames.js`:

```js
import { listProducts } from '@frontscope-fixture/catalog-client';
export async function loadNames() {
  const products = await listProducts();
  return products.map(product => product.name);
}
```

Caller `CatalogPage` apresenta os nomes retornados; usa esta função diretamente sem adaptar a resposta. Nenhum teste, build ou instalação foi executado ou fornecido.
