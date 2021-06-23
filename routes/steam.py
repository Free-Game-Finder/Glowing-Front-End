import requests

free_game_url = "https://raw.githubusercontent.com/Free-Game-Finder/Steam/main/data/free_game_data.json"


def get_json(url):
    return requests.get(url, timeout=10).json()


def get_free_games():

    response = get_json(free_game_url)

    free_games = []

    for key, item in response.items():
        free_games.append({"key": key, "name": item[key]["data"]["name"]})

    return free_games


def get_game_info(game_id):

    response = get_json(
        f"https://store.steampowered.com/api/appdetails?appids={game_id}&cc=US"
    )[game_id]["data"]

    # return {
    #     "game_id": response["steam_appid"],
    #     "name": response["name"],
    #     "required_age": response["required_age"],
    #     "controller_support": response["controller_support"],
    #     "detailed_description": response["detailed_description"],
    #     "about_the_game": response["about_the_game"],
    #     "short_description": response["short_description"],
    #     "header_image": response["header_image"],
    #     "website": response["website"],
    #     "windows": response["platforms"]["windows"],
    #     "mac": response["platforms"]["mac"],
    #     "linux": response["platforms"]["linux"],
    # }

    return response
