// Description: Main js file for the website

// Menu toggle
const menuToggle = document.getElementById('menu-toggle');
const menu = document.getElementsByTagName('nav')[0];


menuToggle.addEventListener('change', function() {
    if (this.checked) {
        menu.classList.add('active');
    } else {
        menu.classList.remove('active');
    }
});
