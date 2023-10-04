import streamlit as st
import requests

# Fonction pour rechercher les restaurants à proximité
def find_restaurants(lat, lon, radius):
    # Clé API Google Maps (vous devez en obtenir une sur https://cloud.google.com/maps-platform/)
    api_key = "VOTRE_CLE_API"

    # URL de l'API Places de Google Maps
    api_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # Paramètres de la requête
    params = {
        "location": f"{lat},{lon}",
        "radius": radius,
        "type": "restaurant",
        "key": api_key
    }

    # Faire la requête à l'API
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        st.error("Une erreur s'est produite lors de la recherche de restaurants.")
        return []

# Interface utilisateur Streamlit
st.title("Trouver des restaurants à proximité")

# Demander à l'utilisateur de saisir les coordonnées et le rayon
lat = st.number_input("Latitude :", min_value=-90.0, max_value=90.0)
lon = st.number_input("Longitude :", min_value=-180.0, max_value=180.0)
radius = st.slider("Rayon de recherche (en mètres) :", 100, 10000, 1000)

if st.button("Rechercher"):
    # Appeler la fonction de recherche de restaurants
    restaurants = find_restaurants(lat, lon, radius)

    # Afficher les résultats
    st.header("Résultats de la recherche :")
    for restaurant in restaurants:
        st.write(restaurant.get("name", "Nom inconnu"))
        st.write("Note :", restaurant.get("rating", "Non évalué"))
        st.write("Adresse :", restaurant.get("vicinity", "Adresse inconnue"))
        st.write("--------------")
