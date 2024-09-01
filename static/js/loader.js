window.addEventListener('load', function() {
    setTimeout(function() {
        document.querySelector('.loader-container').style.display = 'none';
        document.querySelector('.content').style.display = 'block';
    }, 5000); // 5 seconds

    // Typewriter effect for the paragraph
    const text = 'A Product by Social Swirl';
    const paragraphElement = document.querySelector('.paragraph');
    let index = 0;

    function type() {
        if (index < text.length) {
            paragraphElement.textContent += text.charAt(index);
            index++;
            setTimeout(type, 100); // Adjust speed as needed
        }
    }

    // Start typing effect after the page has fully loaded
    type();
});
