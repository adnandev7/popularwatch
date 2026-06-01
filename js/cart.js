function addToCart(id) {
  const watch = typeof getTimepieceById === 'function' ? getTimepieceById(id) : null;
  if (watch) {
    alert(`Added “${watch.name}” to your inquiry bag.`);
  } else {
    alert('Added item to your inquiry bag.');
  }
}
