document.addEventListener('DOMContentLoaded', () => {
  const inquiryForm = document.getElementById('product-inquiry-form');
  if (!inquiryForm) return;

  inquiryForm.addEventListener('submit', (event) => {
    event.preventDefault();
    alert('Your inquiry has been submitted. Our team will contact you shortly.');
    inquiryForm.reset();
  });
});
