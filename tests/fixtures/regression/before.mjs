export function total(subtotal, discountPercent) {
  const percent = discountPercent ?? 10;
  return subtotal * (1 - percent / 100);
}
