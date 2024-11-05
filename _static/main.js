
function playAsciinema(slide) {
    let apWrapper = slide.querySelector(".ap-wrapper");
    if (apWrapper) {
        let enterEvent = new KeyboardEvent("keypress", {
            key: "0",
            keyCode: 48,
            which: 48
        });
        apWrapper.dispatchEvent(enterEvent);

        setTimeout(() => {
            document.querySelector(".ap-wrapper").dispatchEvent(enterEvent);
            slide.querySelector(".ap-playback-button").click();
        }, 500);
    }
}

function addDiv(el, className) {
    var div;
    div = document.createElement('div');
    div.classList = className;
    el.append(div);
    return div;
}

function addLineDivs(el, className) {
    addDiv(el, "line top " + className);
    addDiv(el, "line bottom " + className);
    addDiv(el, "line left " + className);
    addDiv(el, "line right " + className);
}

document.addEventListener("DOMContentLoaded", function(event) {

    Reveal.on('slidechanged', (event) => {
        // event.previousSlide, event.currentSlide, event.indexh, event.indexv
        playAsciinema(event.currentSlide);
        playAsciinema(event.previousSlide);
    });

    /* Add waves to the slides */
    var starBg = document.querySelectorAll("[data-background-hash='0#333333nullnullnullnullnull']");
    for (var i = 0; i < starBg.length; i++) {
        console.log(starBg[i]);
        addDiv(starBg[i], "waves");
    }

    /* Add bubbles to the slides */
    var starBg = document.querySelectorAll("[data-background-hash='0#4973ffnullnullnullnullnull']");
    for (var i = 0; i < starBg.length; i++) {
        console.log(starBg[i]);
        var div = addDiv(starBg[i], "bubbles");
        for (var j = 0; j < 50; j++) {
            addDiv(div, "bubble");
        }
    }

    /* Add hearts to the slides */
    var starBg = document.querySelectorAll("[data-background-hash='0#f18fednullnullnullnullnull']");
    for (var i = 0; i < starBg.length; i++) {
        console.log(starBg[i]);
        var div = addDiv(starBg[i], "hearts");
        for (var j = 0; j < 50; j++) {
            addDiv(div, "heart");
        }
    }

    /* Add Django boxes to the slides */
    var starBg = document.querySelectorAll("[data-background-hash='0#0C4B33nullnullnullnullnull']");
    for (var i = 0; i < starBg.length; i++) {
        console.log(starBg[i]);
        var div = addDiv(starBg[i], "django-boxes");
        for (var j = 0; j < 10; j++) {
            addDiv(div, "box");
        }
    }

    /* Add Angular boxes to the slides */
    var starBg = document.querySelectorAll("[data-background-hash='0#7A03FDnullnullnullnullnull']");
    for (var i = 0; i < starBg.length; i++) {
        console.log(starBg[i]);
        var div = addDiv(starBg[i], "angular-boxes");
        for (var j = 0; j < 10; j++) {
            addDiv(div, "box");
        }
    }

});
