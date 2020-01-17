// $(document).ready(function() {
//     $('.HP-BG-grey-sec').click(function() {
//         $('.particle').hide();
//     });
// });
let particlesSection = document.getElementById('HPsection5');
let particles = document.querySelectorAll('.particles');
let particlesID = document.getElementById('particles')
const colours = ['blue', 'orange', 'green', 'yellow'];
let pos = 0;
let i;

let sectionwWidth = particlesSection.offsetWidth;

let timeOut = 1000;
setTimeout(function () {
    let travellingTime = setInterval(moveParticle, Math.floor(Math.random()*10))

    function moveParticle() {
        if (pos >= sectionwWidth) {
            pos = 0;
        } else {
            pos++;
            particlesID.style.display = "block";
            particlesID.style.right = pos + "px";
            particlesID.style.top = "50px";
        }
    }
}, timeOut);