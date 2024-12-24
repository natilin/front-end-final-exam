from datetime import datetime

import requests
def get_average_death_by_region(top_5: bool=False):
    url = "http://localhost:5000/api/terrorism/average-death-by-region"
    if top_5:
        url += "?top5=true"
    return requests.get(url).json()



def get_all_terror_event():
    return requests.get(
        "http://localhost:5000/api/terrorism/all-terrors").json()


def get_all_events_by_date_range(start_date: str, time_range: int,date_type: str):
    url = "http://localhost:5000/api/terrorism/terror-by-date"
    params = {"time_range": time_range,
              "date_type": date_type,
              "start_date": start_date
              }
    return requests.post(url, params=params).json()


def get_group_with_common_target(country: str=None):
    url = f"http://localhost:5000/api/terrorism/group-with-common-target"
    if country:
        url += f"?country={country}"
    return requests.get(url).json()



def get_most_active_groups_per_country(country: str=None):
    url = f"http://localhost:5000/api/terrorism/most-active-group"
    if country:
        url += f"?country={country}"
    return requests.get(url).json()

def get_most_common_attack_type_per_country(country: str=None):
    url = f"http://localhost:5000/api/terrorism/most-active-targets"
    if country:
        url += f"?country={country}"
        return requests.get(url).json()