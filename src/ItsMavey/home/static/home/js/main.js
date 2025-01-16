const SCROLLBUTTON = document.querySelector('#scrollArrow');


SCROLLBUTTON.addEventListener('click', function() {
    window.scrollTo({
        top: window.innerHeight,
        behavior: 'smooth',
        duration: 5000
    });
});



/* H2 animation */

const headings2 = document.querySelectorAll("main h2");
const headingsArray = Array.from(headings2); // Convert NodeList to array for faster iteration.

let ticking = false;

window.addEventListener("scroll", () => {
    if (!ticking) {
        ticking = true;

        requestAnimationFrame(() => {
            const windowHeight = window.innerHeight;

            headingsArray.forEach(heading2 => {
                const { top } = heading2.getBoundingClientRect();
                const progress = Math.min(Math.max((windowHeight - top) / windowHeight, 0), 1) / 0.5;

                heading2.style.opacity = progress;

                let translateY = 50 - progress * 50;
                if (translateY < 0) translateY = 0;
                heading2.style.transform = `translateY(${translateY}px)`;
            });

            ticking = false;
        });
    }
});

