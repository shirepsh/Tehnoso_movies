from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Load movies data from JSON file
with open("Movies.json", "r") as f:
    movies_data = json.load(f)["movies"]

# Save movies data to JSON file
def save_movies_data():
    with open("Movies.json", "w") as f:
        json.dump({"movies": movies_data}, f, indent=4)

# connect between the html file to the fastAPI 
@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", "r") as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)


@app.get("/movies", response_class=JSONResponse)
async def read_movies():
    movies_with_ratings = []
    for movie in movies_data:
        ratings = movie.get("ratings", [])
        average_rating = sum(ratings) / len(ratings) if ratings else 0
        movie_with_rating = dict(movie)
        movie_with_rating["average_rating"] = average_rating
        movies_with_ratings.append(movie_with_rating)
    return {"movies": movies_with_ratings}

@app.get("/movies/{title}", response_class=JSONResponse)
async def read_movie(title: str):
    for movie in movies_data:
        if movie["title"] == title:
            return movie
    return {"error": "Movie not found"}

@app.post("/movies", response_class=JSONResponse)
async def add_movie(movie: dict):
    # Add movie to movies data
    movies_data.append(movie)
    # Save movies data to JSON file
    save_movies_data()
    # Return the added movie
    return movie

@app.put("/movies/{title}", response_class=JSONResponse)
async def update_movie(title: str, updated_movie: dict):
    for movie in movies_data:
        if movie["title"] == title:
            # Update the movie
            movie.update(updated_movie)
            # Save movies data to JSON file
            save_movies_data()
            # Return the updated movie
            return movie
    return {"error": "Movie not found"}

@app.delete("/movies/{title}", response_class=JSONResponse)
async def delete_movie(title: str):
    for i, movie in enumerate(movies_data):
        if movie["title"] == title:
            # Remove the movie from movies data
            deleted_movie = movies_data.pop(i)
            # Save movies data to JSON file
            save_movies_data()
            # Return the deleted movie
            return deleted_movie
    return {"error": "Movie not found"}

@app.post("/movies/{title}/ratings", response_class=JSONResponse)
async def add_movie_rating(title: str, rating: int):
    for movie in movies_data:
        if movie["title"] == title:
            # Add the rating to the movie's ratings list
            movie.setdefault("ratings", []).append(rating)
            # Save movies data to JSON file
            save_movies_data()
            # Return the updated movie
            return movie
    return {"error": "Movie not found"}
