notes = [
    {"id": 1, "title": "thank you", "text": "hi!"},
    {"id": 2, "title": "thank you2", "text": "hi!2"},
    {"id": 3, "title": "thank you3", "text": "hi!3"},
]

def create_note(note_data: dict):
    max_id = max((note["id"] for note in notes), default=0)
    data = {"id": max_id + 1, "title": note_data["title"],"text": note_data["text"]}
    notes.append(data)
    return notes
create_note({"title": "thank you313", "text": "hi!3134"})
create_note({"title": "thank you313", "text": "hi!3134"})
create_note({"title": "thank you313", "text": "hi!3134"})
create_note({"title": "thank you313", "text": "hi!3134"})
print(notes)