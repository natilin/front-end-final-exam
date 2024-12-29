import pandas as pd

def load_location_csv(csv_path):
    return pd.read_csv(csv_path)


def get_country_coords(country_name: str) -> tuple:
    df = load_location_csv('../data/countries_codes_and_coordinates.csv')
    location = df.loc[df['Country'] == country_name, ['Latitude (average)', 'Longitude (average)']]
    if location.empty:
        return None

    latitude = location.iloc[0]['Latitude (average)'].replace('"', '').strip()
    longitude = location.iloc[0]['Longitude (average)'].replace('"', '').strip()

    return float(latitude), float(longitude)


