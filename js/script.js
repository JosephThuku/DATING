// script.js
const toggleButton = document.getElementById('toggleButton');
const navbar = document.querySelector('.side')
const matchesTab = document.getElementById('match');
const messagesTab = document.getElementById('messo');
const messagesContainer = document.getElementById('messages');
const matchesContainer = document.getElementById('matches');

toggleButton.addEventListener('click', () => {
    if (navbar.style.display === 'none' || navbar.style.display === '') {
        navbar.style.display = 'block';
    } else {
        navbar.style.display = 'none';
    }
});

// Initially hide matches and show messages
matchesContainer.style.display = 'none';
messagesContainer.style.display = 'block';

// Add event listeners to tabs
matchesTab.addEventListener('click', () => {
    matchesContainer.style.display = 'block';
    messagesContainer.style.display = 'none';
});

messagesTab.addEventListener('click', () => {
    matchesContainer.style.display = 'none';
    messagesContainer.style.display = 'block';
});

// Toggle button functionality (you can modify this as needed)
toggleButton.addEventListener('click', () => {
    const navbar = document.querySelector('.menu');
    if (navbar.style.display === 'none' || navbar.style.display === '') {
        navbar.style.display = 'block';
    } else {
        navbar.style.display = 'none';
    }
});
