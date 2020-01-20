let particlesSection = document.getElementById('hp-section5');
let particles = document.querySelectorAll('.particles');
let particlesID = document.getElementById('particles')
const colours = ['blue', 'orange', 'green', 'yellow', 'purple', 'pink', 'black', 'turquoise', 'red'];
let colourPicker = Math.floor(Math.random() * colours.length);
let pos = 0;

let sectionwWidth = particlesSection.offsetWidth;

let timeOut = 1000;
setTimeout(function () {
    let travellingTime = setInterval(moveParticle, Math.floor(Math.random()));
    console.log(travellingTime);

    function moveParticle() {
        
        for (let i = 0; i < particles.length; i++) {
            let randomTop = Math.floor(Math.random() * 10);
            if (pos >= sectionwWidth) {
                pos = 0;
            } else {
                pos++;
                particles[i].style.backgroundColor = colours[colourPicker];
                particles[i].style.position = "absolute";
                particles[i].style.display = "inline-block";
                particles[i].style.right = pos + "px";
                particles[i].style.top = randomTop + "px";
            }
        }
    }
}, timeOut);

// let timeOut = 1000;
// setTimeout(function () {
//     let travellingTime = setInterval(moveParticle, Math.floor(Math.random() * 10+10))

//     function moveParticle() {
//         particles.forEach(particle => {
//             if (pos >= sectionwWidth) {
//                 pos = 0;
//             } else {
//                 pos++;
//                 particle.style.backgroundColor = colours[0];
//                 particle.style.display = "block";
//                 particle.style.right = pos + "px";
//                 particle.style.top = "10px";
//             }
//         });
//     }
// }, timeOut);







// particles[i].addEventListener.one("mouseover", hoverFunc);

// function hoverFunc() {
//     if (true) {
//         pos--;
//         particles[i].style.left = pos + "px";
//     }
// }