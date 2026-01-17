import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

def show_map(place_list):
    """
    Show places on map using Folium
    """
    geolocator = Nominatim(user_agent="student_travel_planner")
    
    # Center map on first place
    location = geolocator.geocode(place_list[0])
    map_osm = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
    
    for place in place_list:
        loc = geolocator.geocode(place)
        if loc:
            folium.Marker([loc.latitude, loc.longitude], tooltip=place).add_to(map_osm)
    
    return map_osm
