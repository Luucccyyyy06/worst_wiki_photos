import requests

api_url = "http://en.wikipedia.org/w/api.php"


params = dict()
params["format"] = "json"
params["action"] = "query"

results = 10
query = "Jet Li"

search_params = {
    "list": "search",
    "srprop": "",
    "srlimit": results,
    "limit": results,
    "srsearch": query,
}

# what other types of params can we use to get different info? list:search but could we get list:info or something?
# then we could directly pull to see if its a disambiguation page or an actual page
query_params = {
    "prop": "info|pageprops",
    "inprop": "url",
    "ppprop": "disambiguation",
    "redirects": "",
}

for k, v in search_params.items():
    params[k] = v

# print(params)
response = requests.get(api_url, params=params)
print(response.text)
