
document.addEventListener('DOMContentLoaded', () => {
    const characterList = document.getElementById('character-list');
    // Function to fetch and display characters based on selected radicals
    async function fetchAndDisplayCharacters() {
        const selectedRadicals = Array.from(document.querySelectorAll('.radical-search.selected'))
            .map(label => label.getAttribute('data-radical-id'));
        try {
            const response = await fetch(`/fetch-characters/?radicals[]=${selectedRadicals.join('&radicals[]=')}`);
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            characterList.innerHTML = '';
            if (data.characters.length > 0) {
                for (const character of data.characters) {
                    const strokeCount = await getStrokeCount(character.name);
                    const div = document.createElement('div');
                    div.className = 'character-item';
                    div.setAttribute('data-character-name', character.name);
                    div.innerHTML = `
                        <h1>${character.name}</h1>
                        <p>${strokeCount !== null ? (strokeCount === 1 ? '1 Stroke' : `${strokeCount} Strokes`) : 'N/A'}</p>
                        <p>${character.meaning}</p>
                    `;
                    characterList.appendChild(div);
                }
            } else {
                characterList.innerHTML = 'No characters found for the selected radicals.';
            }
        } catch (error) {
            console.error('Error fetching characters:', error);
            characterList.innerHTML = 'Error fetching characters.';
        }
    }
    // Function to fetch and parse the KanjiVG SVG file to get stroke count
    async function getStrokeCount(characterName) {
        if (!characterName) {
            console.error('Character name is undefined or null');
            return null;
        }
        const hexCode = encodeURIComponent(characterName.codePointAt(0).toString(16));
        const url = `/static/learn/kanji/0${hexCode}.svg`;
        try {
            const response = await fetch(url);
            if (!response.ok) throw new Error('Network response was not ok');
            const svgText = await response.text();
            const parser = new DOMParser();
            const svgDoc = parser.parseFromString(svgText, "image/svg+xml");
            const pathElements = svgDoc.querySelectorAll("path");
            return pathElements.length; // Assuming each path represents a stroke
        } catch (error) {
            console.error(`Error fetching SVG for character ${characterName}:`, error);
            return null;
        }
    }
    // Event listener for radical selection and deselection
    document.querySelectorAll('.radical-search').forEach(label => {
        label.addEventListener('click', () => {
            label.classList.toggle('selected');
            fetchAndDisplayCharacters();
        });
    });
    // Event listener for character detail navigation
    characterList.addEventListener('click', (event) => {
        const characterName = event.target.getAttribute('data-character-name');
        if (characterName) {
            window.location.href = `/character/${encodeURIComponent(characterName)}/`;
        }
    });
    });
    