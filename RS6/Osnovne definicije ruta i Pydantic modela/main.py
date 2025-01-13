from fastapi import FastAPI, HTTPException, Query
from models import Film, CreateFilm
from typing import List, Optional

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "LOTR: The Fellowship of the Ring", "žanr": "fantasy", "godina": 2001},
    {"id": 2, "naziv": "The Dark Knight", "žanr": "action", "godina": 2008},
    {"id": 3, "naziv": "Interstellar", "žanr": "sci-Fi", "godina": 2014},
]

@app.get("/filmovi", response_model=List[Film])
def get_all_films(genre: Optional[str] = Query(None), min_godina: int = Query(2000)):
    rezultati = [
        Film(**film) for film in filmovi 
        if (genre is None or film["žanr"].lower() == genre.lower()) and film["godina"] >= min_godina]
    return rezultati

@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id: int):
    film = next((film for film in filmovi if film["id"] == id), None)
    if film is None:
        raise HTTPException(status_code=404, detail="film nije pronađen")
    return Film(**film)

@app.post("/filmovi", response_model=Film)
def add_film(film: CreateFilm):
    novi_id = max(f["id"] for f in filmovi) + 1 if filmovi else 1
    novi_film = Film(id=novi_id, **film.dict())
    filmovi.append(novi_film.dict())
    return novi_film
