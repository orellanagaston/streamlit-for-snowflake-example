import streamlit as st
from streamlit_folium import folium_static
import folium
import requests

def obtener_coordenadas(ip_address):
    try:
        # API endpoint y parámetros
        url = f"https://geolocation-db.com/json/{ip_address}"
        response = requests.get(url)
        data = response.json()
        # Extraer las coordenadas
        latitud = data['latitude']
        longitud = data['longitude']
        
        return latitud, longitud
        
    except Exception as e:
        st.error(f"Error al obtener las coordenadas para {ip_address}: {e}")
        return None, None

def main():
    st.title("Geolocalización de Direcciones IP")

    ip_addresses = st.text_area("Ingrese una lista de direcciones IP separadas por coma:")
    ip_list = [ip.strip() for ip in ip_addresses.split(",") if ip.strip()]
    
    if st.button("Obtener Coordenadas"):
        coordenadas = []
        for ip_address in ip_list:
            lat, lon = obtener_coordenadas(ip_address)
            if lat is not None and lon is not None:
                coordenadas.append((lat, lon))
            else:
                st.warning(f"No se pudo obtener la ubicación para la dirección IP: {ip_address}")
        
        if coordenadas:
            # Crear el mapa
            m = folium.Map(location=[coordenadas[0][0], coordenadas[0][1]], zoom_start=5)
            for coord in coordenadas:
                folium.Marker([coord[0], coord[1]], popup=f"Latitud {coord[0]}, Longitud {coord[1]}").add_to(m)
            folium_static(m)
        else:
            st.warning("No se pudieron obtener las coordenadas para ninguna de las direcciones IP.")

if __name__ == "__main__":
    main()
