from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Movie(BaseModel):
    name: str
    classification: str
    release_date: str
    review: str
    season: int

class Character(BaseModel):
    name: str
    movie_or_series: str
    image: str
    description: str

movies_db = []
characters_db = []

@app.post("/movies/")
def create_movie(movie: Movie):
    movies_db.append(movie)
    return movie

@app.get("/movies/", response_model=List[Movie])
def read_movies():
    return movies_db

@app.post("/characters/")
def create_character(character: Character):
    characters_db.append(character)
    return character

@app.get("/characters/", response_model=List[Character])
def read_characters():
    return characters_db
