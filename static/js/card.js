document.addEventListener('DOMContentLoaded', () => {
    // Get all card containers
    const cardContainers = document.querySelectorAll('.swip_component');

    cardContainers.forEach(container => {
        const cards = Array.from(container.querySelectorAll('.swipe_clothe'));
        let currentIndex = 0;

        function showNextCard() {
            // Remove 'hidden' class from all cards and reset z-index
            cards.forEach(card => {
                card.classList.remove('hidden');
                card.style.zIndex = '';
            });

            // Update index and handle looping
            currentIndex++;
            if (currentIndex >= cards.length) {
                currentIndex = 0;
            }

            // Bring the new card to the front
            const nextCard = cards[currentIndex];
            nextCard.style.zIndex = cards.length; // Set z-index to the highest value

            // Update z-index and transform for each card
            cards.forEach((card, index) => {
                // Adjust z-index so that the next card is at the top
                card.style.zIndex = cards.length - (index + 1 + cards.length - currentIndex) % cards.length;

                // Apply transforms based on their position relative to the current card
                const position = (index - currentIndex + cards.length) % cards.length;
                const rotationAngles = [0, 15, -20];
                card.style.transform = `rotate(${rotationAngles[position]}deg)`;
            });
        }

        // Initialize z-index and rotation
        updateCardZIndex();

        // Add click event to each card
        cards.forEach(card => {
            card.addEventListener('click', showNextCard);
        });

        function updateCardZIndex() {
            cards.forEach((card, index) => {
                card.style.zIndex = cards.length - index;
                card.style.transform = `rotate(${0 + (index * 15)}deg)`;
            });
        }
    });
});
