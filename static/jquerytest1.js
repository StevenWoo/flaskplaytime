var notes = [
  {id: 1, body: "This is a first test", timestamp: Date.now()},
  {id: 2, body: "This is a second test", timestamp: Date.now()},
  {id: 3, body: "This is a third test", timestamp: Date.now()}
];

notes.forEach(function(note) {
  $('.note-selectors').append(
    '<div class="note-selector">' +
      '<p class="note-selector-title">' + note.body + '</p>' +
      '<p class="note-selector-timestamp">' + note.timestamp + '</p>' +
    '</div>'
  );
});
