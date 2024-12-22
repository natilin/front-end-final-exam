import requests
def get_average_death_by_region(top_5: bool=False):
    url = "http://localhost:5000/api/terrorism/average-death-by-region"
    if top_5:
        url += "?top5=true"
    return requests.get(url).json()

