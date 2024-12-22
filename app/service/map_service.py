
import folium

from app.api.api import get_average_death_by_region

average_death_by_region = get_average_death_by_region()


m = folium.Map(location=[0, 0], zoom_start=2)


for region in average_death_by_region:
    popup_text = f"{region['region']}: 'average_deadly_rating': {region['average_deadly_rating']}, 'num_of_attack': {region['num_of_attack']}"
    folium.Marker(
        location=[region['latitude'], region['longitude']],
        popup=popup_text
    ).add_to(m)

m.save("map.html")