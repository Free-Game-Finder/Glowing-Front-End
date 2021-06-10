import requests

free_game_url = 'https://raw.githubusercontent.com/Free-Game-Finder/Steam/main/data/free_game_data.json'


def get_json(url):
    return requests.get(url, timeout=10).json()


def get_free_games():

    response = get_json(free_game_url)

    free_games = []

    for key, item in response.items():
        free_games.append(
            {
                "key": key,
                "name": item[key]["data"]["name"]
            }
        )

    return free_games
