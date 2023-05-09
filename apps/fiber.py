import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Fiber Links")

    m = leafmap.Map(center=[80, 40], zoom=4)

    in_geojson = 'https://raw.githubusercontent.com/desilvarami/thhydro/main/cable_geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")

    m.to_streamlit(height=400)
