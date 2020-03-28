$(document).ready(function () {
    for (let i = 0; i < 5; i++) {
        $(".particles-area").append("<div class='col-12 single-particle'></div>");
        $(".single-particle").append("<div class='particles'></div>");
    }
    
    let particlesSection = document.getElementById('hp-section4');
    let particles = document.querySelectorAll('.particles');
    let sectionHeight = particlesSection.clientHeight;
    let sectionWidth = particlesSection.clientWidth - 10;
    const colours = ['blue', 'orange', 'green', 'yellow', 'purple', 'pink', 'black', 'turquoise', 'red'];
    
    particles.forEach(particle => {
        let randomInterval = Math.floor((Math.random() * 10)) + 1;
        let currentTop = Math.floor(Math.random() * sectionHeight) / 1.2;
        let currentRight = Math.floor(Math.random() * sectionWidth) + 1;
        let colourPicker = Math.floor(Math.random() * colours.length);
        let animationSpeed = Math.random() + 1;
    
        setInterval(moveParticle, randomInterval);
    
        function moveParticle() {
            particle.style.backgroundColor = colours[colourPicker];
            particle.style.top = currentTop + "px";
            particle.style.right = currentRight + "px";
            particle.style.animationDuration = animationSpeed + "s";
            if (currentRight >= sectionWidth) {
                currentRight = 10;
            } else {
                currentRight++;
            }
        }
    });
});

// let particlesSection = document.getElementById('hp-section5');
// let particles = document.querySelectorAll('.particles');
// let particlesID = document.getElementById('particles')
// const colours = ['blue', 'orange', 'green', 'yellow', 'purple', 'pink', 'black', 'turquoise', 'red'];
// let colourPicker = Math.floor(Math.random() * colours.length);
// let pos = 0;

// let sectionwWidth = particlesSection.offsetWidth;

// let timeOut = 1000;
// setTimeout(function () {
//     let randomInterval = Math.floor((Math.random() * 10)) + 1;
//     console.log(randomInterval);
//     let travellingTime = setInterval(moveParticle, randomInterval);

//     function moveParticle() {

//         for (let i = 0; i < particles.length; i++) {
//             let randomTop = Math.floor(Math.random() * 10);
//             if (pos >= sectionwWidth) {
//                 pos = 0;
//             } else {
//                 pos++;
//                 particles[i].style.backgroundColor = colours[colourPicker];
//                 particles[i].style.position = "absolute";
//                 particles[i].style.display = "inline-block";
//                 particles[i].style.right = pos + "px";
//             }
//         }
//     }
// }, timeOut);

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
