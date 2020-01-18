let particlesSection = document.getElementById('hp-section5');
let particles = document.querySelectorAll('.particles');
let particlesID = document.getElementById('particles')
const colours = ['blue', 'orange', 'green', 'yellow'];
let pos = 0;
let i;

let sectionwWidth = particlesSection.offsetWidth;

let timeOut = 1000;
setTimeout(function () {
    let travellingTime = setInterval(moveParticle, Math.floor(Math.random() * 10+10))

    function moveParticle() {
        particles.forEach(particle => {
            if (pos >= sectionwWidth) {
                pos = 0;
            } else {
                pos++;
                particle.style.backgroundColor = colours[0];
                particle.style.display = "block";
                particle.style.right = pos + "px";
                particle.style.top = "10px";
            }
        });
    }
}, timeOut);