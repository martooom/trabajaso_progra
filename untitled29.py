# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pBRZcsZSrVuOqqSv0fP8RIFpx5vfQbdV
"""

import streamlit as st
from PIL import Image
import pandas as pd
import altair
st.title("cantidad  de terremotos en chile")

image= Image.open("terremoto.jpg")
st.image(image, caption="terremoto", use_column_width=True)

st.sidebar.title("barra lateral")
st.sidebar.write("esto es una barra lateral")

if st.sidebar.button(" haz clik hay unos tips")
  st.sidebar.write("Mantente alejado de ventanas, espejos y muebles grandes, Si el edificio es estructuralmente endeble, sal de él lo más rápido posible. Si estas afuera, corre a un área abierta lejos de edificios y cableado eléctrico que pueda caer sobre ti.")

user_input = st.sidebar.text_input("Escribe algo en la barra:")
st.siidebar.write(f"has escrito: {user_input}")

st.title("Estadisticas desde 2010 hasta hoy en dia")
data={"Años":[2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023], "cantidad de terremotos":[300, 1500, 2000, 2500, 2300, 2500, 3000, 2800]}
df=pd.DataFrame(data)
st.write(df)

chart=altair.Chart(df).mark_bar().encode(
  x="Años:O",
  y="cantidad de terremotos:Q"
)