# service.py
"""
Service layer (FastAPI).

HOSTING INSTRUCTIONS:
Run locally with:
    pip install -r requirements.txt
    uvicorn service:app --reload --port 8000

Platform note:
Local hosting with uvicorn satisfies the hosting requirement for many classes.
If you choose a cloud host later, keep these instructions + add your platform steps.
"""

from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from business import BusinessLayer

app = FastAPI(title="CSCE548 Project 2 - Movie Watchlist Service")
bl = BusinessLayer()


# ----------- Models -----------
class MovieIn(BaseModel):
    title: str
    release_year: int
    runtime_minutes: Optional[int] = None
    genre: Optional[str] = None


class ListIn(BaseModel):
    name: str
    description: Optional[str] = None
    is_public: bool = False


# ----------- Movie endpoints -----------
@app.get("/movies")
def list_movies():
    return bl.list_movies()

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    m = bl.get_movie_by_id(movie_id)
    if not m:
        raise HTTPException(status_code=404, detail="Movie not found")
    return m

@app.post("/movies")
def create_movie(movie: MovieIn):
    try:
        movie_id = bl.create_movie(movie.title, movie.release_year, movie.runtime_minutes, movie.genre)
        return {"movie_id": movie_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: MovieIn):
    try:
        ok = bl.update_movie(movie_id, movie.title, movie.release_year, movie.runtime_minutes, movie.genre)
        return {"updated": ok}
    except ValueError as e:
        # If it's "not found", treat as 404; otherwise 400
        msg = str(e)
        raise HTTPException(status_code=404 if "not found" in msg.lower() else 400, detail=msg)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    try:
        ok = bl.delete_movie(movie_id)
        return {"deleted": ok}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# ----------- List endpoints -----------
@app.get("/users/{user_id}/lists")
def list_lists_by_user(user_id: int):
    return bl.list_lists_by_user(user_id)

@app.post("/users/{user_id}/lists")
def create_list(user_id: int, lst: ListIn):
    try:
        list_id = bl.create_list(user_id, lst.name, lst.description, lst.is_public)
        return {"list_id": list_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/lists/{list_id}")
def update_list(list_id: int, lst: ListIn):
    try:
        ok = bl.update_list(list_id, lst.name, lst.description, lst.is_public)
        return {"updated": ok}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/lists/{list_id}")
def delete_list(list_id: int):
    ok = bl.delete_list(list_id)
    return {"deleted": ok}

@app.get("/lists/{list_id}/items")
def list_items_for_list(list_id: int):
    return bl.list_items_for_list(list_id)

