document.addEventListener('DOMContentLoaded', () => {
  const menuButton = document.getElementById('mobile-menu-btn');
  const closeButton = document.getElementById('close-mobile-menu-btn');
  const mobilePanel = document.getElementById('mobile-nav-panel');

  if (!menuButton || !closeButton || !mobilePanel) return;

  menuButton.addEventListener('click', () => {
    mobilePanel.classList.remove('translate-x-full');
  });

  closeButton.addEventListener('click', () => {
    mobilePanel.classList.add('translate-x-full');
  });
});