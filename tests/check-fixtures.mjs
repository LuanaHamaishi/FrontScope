// Checks JavaScript fixture assumptions, not agent behavior.
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
console.log('OK: zero-discount regression reproduced (base=100, candidate=90).');
console.log('OK: negative control preserves output for all 5 checked inputs.');
console.log('These checks validate fixtures, not model decisions or agent compatibility.');
