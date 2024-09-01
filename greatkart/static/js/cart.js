// /templates/js/cart.js

document.addEventListener('DOMContentLoaded', () => {
    const increaseButtons = document.querySelectorAll('.increase');
    const decreaseButtons = document.querySelectorAll('.decrease');
    const cartCountElement = document.querySelector('.cart-count');

    // Function to update cart count
    const updateCartCount = () => {
        let cartCount = 0;
        const countElements = document.querySelectorAll('.product-item .count');
        countElements.forEach(element => {
            cartCount += parseInt(element.textContent, 10);
        });
        cartCountElement.textContent = cartCount;
    };

    // Add event listeners to increase buttons
    increaseButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const countElement = event.target.previousElementSibling;
            let count = parseInt(countElement.textContent, 10);
            count += 1;
            countElement.textContent = count;
            updateCartCount();
        });
    });

    // Add event listeners to decrease buttons
    decreaseButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const countElement = event.target.nextElementSibling;
            let count = parseInt(countElement.textContent, 10);
            if (count > 0) { // Ensure count doesn't go below 0
                count -= 1;
                countElement.textContent = count;
                updateCartCount();
            }
        });
    });

    // Initial cart count update
    updateCartCount();
});
