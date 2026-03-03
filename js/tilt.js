/**
 * Vanilla Tilt Implementation
 * Adds a subtle 3D tilt effect to cards
 */
function initTilt(selector) {
    const cards = document.querySelectorAll(selector);

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within element
            const y = e.clientY - rect.top;  // y position within element

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            // Calculate rotation based on cursor position
            // Max rotation of 10 degrees
            const rotateX = ((y - centerY) / centerY) * -10;
            const rotateY = ((x - centerX) / centerX) * 10;

            // Apply transformation
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
        });

        card.addEventListener('mouseleave', () => {
            // Reset with transition
            card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)`;
        });
    });
}

// Initialize for different sections
document.addEventListener('DOMContentLoaded', () => {
    initTilt('.practice-card');
    initTilt('.why-card');
    initTilt('.blog-card'); // Matches publications/blog page
});
