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