import requests
import ast
import wikipedia
from rich import print

# set rate_limting, to enable/disable rate limiting on requests to servers, to avoid HTTP timeout error.
wikipedia.set_rate_limiting(rate_limit=True)

api_url = "http://en.wikipedia.org/w/api.php"


def get_response_title(
    api_url: str, params: dict, number_of_results: int, celebrity_name: str
):
    params["srsearch"] = f"{celebrity_name}"
    params["limit"] = number_of_results
    response = requests.get(api_url, params=params)
    response_text = ast.literal_eval(response.text)
    response_title = response_text["query"]["search"][0]["title"]
    return response_title


params = {
    "action": "query",
    "prop": "images",
    "prop": "info",
    "list": "search",
    "format": "json",
}
for k, v in params.items():
    params[k] = v

celebrity_list = [
    "Rufus Sewell",
    "Paul Mescal",
    "Charlize Theron",
    "Jet Li",
    "Usher",
    "Daniel Radcliffe",
    "Beyonce",
]

celebrity_names_and_photos = {}
for celebrity in celebrity_list:
    celebrity_page_name = get_response_title(api_url, params, 3, celebrity)
    celebrity_names_and_photos[celebrity] = {
        "name": celebrity_page_name,
        "image": wikipedia.page(f"{celebrity_page_name}").images[0],
    }

print(celebrity_names_and_photos)
