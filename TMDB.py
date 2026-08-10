#List of functions used to get data from the TMDB API

#Get the numbers for the primary and secondary data from the TMDB API for a given movie ID
# (primary data: score, revenue, runtime, release date)
# (secondary data: vote count, budget, popularity)
def get_movie_data(tmdb_id):
    import os
    from dotenv import load_dotenv
    import requests
    from datetime import date

    load_dotenv()

    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_TOKEN')}"
    }

    response = requests.get(url, headers=headers)

    output = {
        "score": float(response.json()['vote_average']),
        "revenue": int(response.json()['revenue']),
        "runtime": int(response.json()['runtime']),
        "release_date": date.fromisoformat(response.json()['release_date']),
        "vote_count": int(response.json()['vote_count']),
        "budget": int(response.json()['budget']),
        "popularity": float(response.json()['popularity'])
    }
    return output