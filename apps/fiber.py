import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Fiber Links")

    m = leafmap.Map(center=[6,0], zoom=2)

    in_geojson = 'https://raw.githubusercontent.com/desilvarami/thhydro/main/cable_geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")

    m.to_streamlit(height=400)
