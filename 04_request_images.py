import requests
import ast
import wikipedia
from rich import print

# set rate_limting, to enable/disable rate limiting on requests to servers, to avoid HTTP timeout error.
wikipedia.set_rate_limiting(rate_limit=True)

api_url = "http://en.wikipedia.org/w/api.php"


def get_response_title(api_url: str, params: dict, number_of_results: int, celebrity_name: str):
    params['query'] = f'{celebrity_name}'
    params['results'] = 
    
    response = requests.get(api_url, params=params)
    response_text = ast.literal_eval(response.text)
    response_title = response_text["query"]["search"][0]["title"]
    return response_title
results = 3
query = "Tom Jones"

params = {
    "action": "query",
    "prop": "images",
    "prop": "info",
    "list": "search",
    "format": "json",
    "srlimit": results,
    "limit": results,
    "srsearch": query,
}
for k, v in params.items():
    params[k] = v



def get_response_title(api_url: str, params: dict, ):
    response = requests.get(api_url, params=params)
    response_text = ast.literal_eval(response.text)
    response_title = response_text["query"]["search"][0]["title"]
    return response_title


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
    celebrity_page_name = get_response_title(api_url, params)
    celebrity_names_and_photos[celebrity] = {
        "name": celebrity_page_name,
        "image": wikipedia.page(f"{celebrity_page_name}").images[0],
    }

print(celebrity_names_and_photos)
