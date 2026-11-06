export function label(count) {
  const message = count === 1 ? '1 item' : `${count} items`;
  return message;
}
