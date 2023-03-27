import requests
import ast

api_url = "http://en.wikipedia.org/w/api.php"

params = dict()
params["format"] = "json"
params["action"] = "query"

results = 3
query = "Beyonce"

search_params = {
    "list": "search",
    "srprop": "",
    "srlimit": results,
    "limit": results,
    "srsearch": query,
}

for k, v in search_params.items():
    params[k] = v

response = requests.get(api_url, params=params)
response_text = ast.literal_eval(response.text)
print("##########")
print(response_text)
print("##########")
print(response_text["query"]["search"][0])


# what other types of params can we use to get different info? list:search but could we get list:info or something?
# then we could directly pull to see if its a disambiguation page or an actual page
query_params = {
    "prop": "info|pageprops",
    "inprop": "url",
    "ppprop": "disambiguation",
    "redirects": "",
}
print("##########")
print("TEST PARAMS")
print("##########")
test_params = {
    "action": "query",
    "prop": "images",
    "prop": "info",
    "list": "search",
    "format": "json",
}

for k, v in test_params.items():
    params[k] = v

response = requests.get(api_url, params=params)
response_text = ast.literal_eval(response.text)
print("##########")
print(response_text)
print("##########")
print(response_text["query"])
