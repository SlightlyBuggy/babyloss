var SOURCES_COLLAPSED_TEXT = "Show Sources"
var SOURCES_EXPANDED_TEXT = "Hide Sources"

$(document).ready(function() {
    console.log("doing this")
    $('#sources_button').text(SOURCES_COLLAPSED_TEXT)
}) 

$(document).on('click', '#sources_button', function() {
    var new_text = $('#sources_button').text().trim() === SOURCES_COLLAPSED_TEXT ? SOURCES_EXPANDED_TEXT : SOURCES_COLLAPSED_TEXT
    $('#sources_button').text(new_text)
})