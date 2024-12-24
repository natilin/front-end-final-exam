from datetime import datetime
import folium
from folium.plugins import HeatMap
from app.api.api import get_average_death_by_region, get_all_terror_event, get_all_events_by_date_range, \
    get_group_with_common_target, get_most_active_groups_per_country


def get_default_map():
    return folium.Map(location=[0, 0], zoom_start=2)


def get_average_death_map(top_5=False):
    average_death_by_region = get_average_death_by_region(top_5)
    m = folium.Map(location=[0, 0], zoom_start=2)
    for region in average_death_by_region:
        popup_text = f"{region['region']}: 'average_deadly_rating': {region['average_deadly_rating']}, 'num_of_attack': {region['num_of_attack']}"
        folium.Marker(
            location=[region['latitude'], region['longitude']],
            popup=popup_text
        ).add_to(m)

    return m


def get_all_terror_event_map(start_date: str = None, time_range: int = None, date_type: str = None):
    if start_date is None:
        all_terror_event = get_all_terror_event()
    else:
        all_terror_event = get_all_events_by_date_range(start_date=start_date, time_range=time_range,
                                                        date_type=date_type)

    m = folium.Map(location=[0, 0], zoom_start=2)
    heat_data = [[event["location"]['latitude'], event["location"]['longitude']] for event in all_terror_event]
    HeatMap(heat_data).add_to(m)
    return m


def get_group_with_common_target_map(country: str = None):
    all_target = get_group_with_common_target(country)
    m = folium.Map(location=[0, 0], zoom_start=2)
    for region in all_target:
        popup_text = f"country:{region['country']} groups_name:{region['groups_name']}"
        try:
            folium.Marker(
                location=[region['latitude'], region['longitude']],
                popup=popup_text
            ).add_to(m)
        except:
            pass

    m.save("mapp.html")



def get_most_active_groups_per_country_map(country: str = None):
    all_groups = get_most_active_groups_per_country(country)
    m = folium.Map(location=[0, 0], zoom_start=2)
    for country in all_groups:
        group_list = list(map(lambda x: x['group'] ,country['top_groups']))
        popup_text = f"country:{country['_id']} top 5 group:{group_list}"
        latitude = country['top_groups'][0]['latitude']
        longitude = country['top_groups'][0]['longitude']
        try:
            folium.Marker(
                location=[latitude , longitude],
                popup=popup_text
            ).add_to(m)
        except:
            pass

    m.save("mapp.html")

