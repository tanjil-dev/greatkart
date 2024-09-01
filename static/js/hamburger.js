document.addEventListener("DOMContentLoaded", function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mobileNav = document.querySelector('.mobile-nav');
    const closeBtn = document.querySelector('#close-btn');

    hamburgerMenu.addEventListener('click', function() {
        this.classList.toggle('open');
        mobileNav.classList.toggle('open');
    });

    closeBtn.addEventListener('click', function() {
        hamburgerMenu.classList.remove('open');
        mobileNav.classList.remove('open');
    });
});
