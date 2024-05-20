$(document).ready(function() {
    // Add a click event listener to all buttons with class 'play-kana'
    $('.play-kana').click(function() {
        var character;

        // Check if there's an SVG inside the .display-kana
        var svgInsideDisplayKana = $(this).closest('.display-kana').find('svg').length > 0;

        if (svgInsideDisplayKana) {
            // If there's an SVG inside .display-kana, get the character associated with the SVG
            character = $(this).closest('.display-kana').find('span').text();
        } else {
            // If there's no SVG inside .display-kana, get the character associated with the .play-kana button
            character = $(this).find('span').text();
        }

        // Make an AJAX request to generate and play audio
        $.ajax({
            url: '/generate_audio/',
            method: 'GET',
            data: { character: character },
            xhrFields: {
                responseType: 'blob'  // Set response type to 'blob' to handle binary data
            },
            success: function(data) {
                // Create a URL for the audio blob data
                var audioUrl = URL.createObjectURL(data);
                // Create an <audio> element to play the audio
                var audioElement = new Audio(audioUrl);
                // Play the audio
                audioElement.play();
            },
            error: function(xhr, status, error) {
                console.error('Error generating audio:', error);
            }
        });
    });
});
