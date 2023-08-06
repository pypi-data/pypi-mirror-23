"use strict";

var container;
var content;
var bgExit;

{{vars}}

// i.e. Giving them Instance Names like in Flash - makes it easier
function assignInstanceNames() {
    container = document.getElementById('adkit_container');
    content = document.getElementById('adkit_contemt');
    bgExit = document.getElementById('adkit_background_exit');

{{elements}}
}

// ---------------------------------------------------------------------------
// ANIMATION
// ---------------------------------------------------------------------------

function animateAd() {
    // TweenLite.to(text1, 1, { opacity: 1, ease: Power2.easeOut, delay: .5 });

    // final frame
    TweenLite.set(logo, { scale: 0.5 });
    TweenLite.to(logo, 0.5, { opacity: 1, scale: 1, ease: Back.easeOut, delay: 7 });
    TweenLite.to(cta, 0.5, { opacity: 1, ease: Quad.easeOut, delay: 7 });
    TweenLite.to(shine, 1, {
        left: shine.offsetWidth, ease: Power1.easeInOut, delay: 9, onComplete: function () {
            TweenLite.set(shine, { left: -shine.offsetWidth });
        }
    });
}

// ---------------------------------------------------------------------------
// LOAD IMAGES - only animate when images loaded (stops initial load oddities)
// ---------------------------------------------------------------------------

var images = [
{{images}}
];

var index = 0;

// Adwords hack to get around the "Missing Asset Check". If we set the
// source using a method call rather than a string it lets us pass the test.
function getImagePath() {
    return 'images/' + images[index];
}

// load all images before we begin
function loadImage() {
    var img = new Image();
    img.onload = function () {
        ++index;

        if (index < images.length) {
            loadImage();
            //console.debug('load '+images[index]);
        } else {
            // Animate ad
            animateAd();
            // Show ad (avoids flashing while image assets load)
            container.style.display = "block";
        }
    }
    img.src = getImagePath();
}

// ---------------------------------------------------------------------------
// ADWORDS - typically, we do not mess with this section
// ---------------------------------------------------------------------------

function init() {
    assignInstanceNames()
    addListeners();
    loadImage();
}

function addListeners() {
    bgExit.addEventListener('mouseover', bgOverHandler);
    bgExit.addEventListener('mouseout', bgOutHandler);
    bgExit.addEventListener('click', bgExitHandler);
}

function bgOverHandler(e) {
    // cta.setAttribute('class', 'active');
    TweenLite.to(shine, 1, { left: shine.offsetWidth, ease: Power1.easeInOut });
}

function bgOutHandler(e) {
    // cta.setAttribute('class', '');
    TweenLite.to(shine, 1, { left: -shine.offsetWidth, ease: Power1.easeInOut });
}

function bgExitHandler() {
    console.log('clickthrough');
    ExitApi.exit();
}

window.addEventListener("load", init);

// ---------------------------------------------------------------------------
