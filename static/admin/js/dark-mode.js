// dark-mode.js
document.addEventListener('DOMContentLoaded', function () {
    const toggle = document.getElementById('dark-mode-switch');
    if (toggle) {
        toggle.addEventListener('change', function () {
            document.body.classList.toggle('dark-mode', toggle.checked);
            // Save preference
            localStorage.setItem('dark-mode', toggle.checked);
        });

        // Set initial state
        const isDarkMode = localStorage.getItem('dark-mode') === 'true';
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            toggle.checked = true;
        }
    }
});
