document.addEventListener('DOMContentLoaded', function () {
    const icon = document.getElementById('dark-mode-icon');

    if (icon) {
        icon.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');

            // Toggle between sun and moon icons
            if (document.body.classList.contains('dark-mode')) {
                icon.src = "{% static 'admin/img/icon-moon.svg' %}";
            } else {
                icon.src = "{% static 'admin/img/icon-sun.svg' %}";
            }

            // Save user preference
            localStorage.setItem('dark-mode', document.body.classList.contains('dark-mode'));
        });

        // Set initial state based on user preference
        const isDarkMode = localStorage.getItem('dark-mode') === 'true';
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            icon.src = "{% static 'admin/img/icon-moon.svg' %}";
        } else {
            icon.src = "{% static 'admin/img/icon-sun.svg' %}";
        }
    }
});
