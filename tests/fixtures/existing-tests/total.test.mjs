import assert from 'node:assert/strict';
import test from 'node:test';
import { total } from '../src/total.mjs';

test('zero means no discount', () => {
  assert.equal(total(100, 0), 100);
});

test('missing discount selects the existing default', () => {
  assert.equal(total(100, undefined), 90);
  assert.equal(total(100, null), 90);
});

test('explicit discounts retain their meaning', () => {
  assert.equal(total(100, 25), 75);
});
