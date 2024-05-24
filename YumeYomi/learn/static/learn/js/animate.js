'use strict';

document.addEventListener('DOMContentLoaded', async function () {

    // Define the KVGAnimator class
    var KVGAnimator = function () {
        function t(t) {
            this.time = t;
        }
        return t.prototype.play = async function (t) {
            var e = this.findTarget(t);
            if (e && "svg" === e.tagName && !(e.querySelectorAll("path") <= 0)) {
                this.paths = e.querySelectorAll("path");
                this.numbers = e.querySelectorAll("text");
                this.pathCount = this.paths.length;
                this.hideAll();
                for (var i = 0; i < this.pathCount; i++) {
                    await this.animatePath(this.paths[i], this.numbers[i]);
                }
            }
        }, t.prototype.findTarget = function (t) {
            var e = "data-kanjivg-target";
            if (!t.hasAttribute(e)) return t;
            var i = t.getAttribute(e);
            return document.querySelector(i);
        }, t.prototype.hideAll = function () {
            for (var t = 0; t < this.pathCount; t++) {
                this.paths[t].style.display = "none";
                if ("undefined" != typeof this.numbers[t]) {
                    this.numbers[t].style.display = "none";
                }
            }
        }, t.prototype.animatePath = function (t, e) {
            return new Promise(resolve => {
                var length = t.getTotalLength();
                t.style.display = "block";
                if ("undefined" != typeof e && document.getElementById('show-strokes').checked) {
                    e.style.display = "block";
                }
                t.style.transition = t.style.WebkitTransition = "stroke-dashoffset " + this.time + "ms linear";
                t.style.strokeDasharray = length + " " + length;
                t.style.strokeDashoffset = length;
                setTimeout(function () {
                    t.style.strokeDashoffset = "0";
                    resolve();
                }, this.time);
            });
        }, t;
    }();

    // Function to load an SVG file
    async function loadSVG(url) {
        const response = await fetch(url);
        const text = await response.text();
        return new DOMParser().parseFromString(text, "image/svg+xml").documentElement;
    }

    // Function to display a single Kanji character
    async function displayKanji(char) {
        const svg = await loadSVG(`/static/learn/kanji/0${char.codePointAt(0).toString(16)}.svg`);
        return svg;
    }

    // Function to display a phrase with stroke order
    async function displayPhrase(phrase) {
        const container = document.getElementById('kanji-container');
        container.innerHTML = ''; // Clear previous content
        const chars = [...phrase]; // Split the phrase into individual characters

        let animator = null;
        for (const char of chars) {
            const svg = await displayKanji(char);
            container.appendChild(svg); // Append SVG to the container
            animator = new KVGAnimator(500); // Adjust duration as needed
            await animator.play(svg);
        }
    }

    // Play button event listener
    document.getElementById('play-button').addEventListener('click', async function () {
        // Get the Kanji text from the hidden span
        const kanjiText = document.getElementById('kanji-text').textContent;
        await displayPhrase(kanjiText);
    });

    // Checkbox event listener
    document.getElementById('show-strokes').addEventListener('change', function () {
        const strokesVisible = document.getElementById('show-strokes').checked;
        const numbers = document.querySelectorAll('#kanji-container text');
        numbers.forEach(number => {
            if (strokesVisible) {
                number.style.display = 'block';
            } else {
                number.style.display = 'none';
            }
        });
    });

});
