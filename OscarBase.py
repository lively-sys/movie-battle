#List of functions used to get data from the OscarBase API

#Gets the number of unique oscar nominations and wins for a movie given its TMDB ID
def get_nominations(tmdb_id):
    import requests

    solo_awards=["Directing","Actor In A Leading Role","Actor In A Supporting Role","Actress In A Leading Role","Actress In A Supporting Role"]

    url_a = "https://api.oscarbase.com/api/movies"
    params = {
        "tmdb_id": tmdb_id
    }
    response = requests.get(url_a, params=params)

    if response.json()['pagination']['total'] == 0:
        return {"noms": 0, "wins": 0}

    url_b=f"https://api.oscarbase.com/api/movies/{response.json()['data'][0]['id']}"

    nominations = requests.get(url_b).json()["data"]["nominations"]
    unique_nominations = []
    seen_categories = set()

    for nomination in nominations:
        if nomination["category"] in solo_awards or nomination["category"] not in seen_categories:
            unique_nominations.append(nomination)
            seen_categories.add(nomination["category"])
    unique_winners = [
        nomination
        for nomination in unique_nominations
        if nomination["winner"]
    ]

    return {"noms": len(unique_nominations), "wins": len(unique_winners)}