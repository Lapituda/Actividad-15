from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

class Note(BaseModel):
    title: str
    author: str
    body: str
    classification: str
    created_at: datetime = datetime.now()

notes_db = []

@app.post("/notes/")
def create_note(note: Note):
    notes_db.append(note)
    return note

@app.get("/notes/", response_model=List[Note])
def read_notes():
    return notes_db

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    if note_id < len(notes_db):
        notes_db[note_id] = note
        return note
    else:
        raise HTTPException(status_code=404, detail="Note not found")

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id < len(notes_db):
        deleted_note = notes_db.pop(note_id)
        return deleted_note
    else:
        raise HTTPException(status_code=404, detail="Note not found")
