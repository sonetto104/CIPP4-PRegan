const floatingButton = document.querySelector('.floating-button');
const message = document.querySelector('.message');

floatingButton.addEventListener('mousemove', (e) => {
    const rect = floatingButton.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    message.style.transform = `translate(${x}px, ${y}px)`;
});