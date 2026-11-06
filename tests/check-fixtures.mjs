// Verifica a verdade dos exemplos JS; não mede comportamento de um agente.
import assert from 'node:assert/strict';
import { total as before } from './fixtures/regression/before.mjs';
import { total as after } from './fixtures/regression/after.mjs';
import { label as cleanBefore } from './fixtures/clean/before.mjs';
import { label as cleanAfter } from './fixtures/clean/after.mjs';

assert.equal(before(100, 0), 100);
assert.equal(after(100, 0), 90);
for (const value of [null, undefined, 10, 100]) {
  assert.equal(before(100, value), after(100, value));
}
for (const count of [0, 1, 2, 10, 1000]) {
  assert.equal(cleanBefore(count), cleanAfter(count));
}
console.log('OK: regressão de zero reproduzida (base=100, candidata=90).');
console.log('OK: controle negativo preserva saída nas 5 entradas verificadas.');
console.log('Estes checks validam fixtures, não decisões do modelo nem compatibilidade de agentes.');
