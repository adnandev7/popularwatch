function addToCart(id) {
  // Deprecated: cart functionality replaced by Buy Now (WhatsApp). Preserve for compatibility.
  const watch =
    typeof getTimepieceById === "function" ? getTimepieceById(id) : null;
  if (watch) {
    console.warn(
      "addToCart called but replaced by Buy Now flow. Redirect user to WhatsApp instead.",
    );
  }
}
