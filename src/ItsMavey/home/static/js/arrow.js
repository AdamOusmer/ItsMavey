const SCROLL_WORD = "Scroll Down";
const SCROLL_DOT = "•";
const SCROLL_WORD_REPEAT = 3;

const SCROLL_TEXT_CONTAINER = document.getElementById('text-container-scrollArrow');

SCROLL_WORD.split("").forEach((char, i) => {

    for (let j = 0; j < SCROLL_WORD_REPEAT; j++) {
        function createText(offset) {
            const text = document.createElement('div');
            text.classList.add('text');
            text.textContent = char;
            SCROLL_TEXT_CONTAINER.appendChild(text)
        }
        function createDot(offset) {
            const dot = document.createElement('div');
            dot.classList.add('dot');
            document.getElementById('scroll').appendChild(dot);
        }
    }
});