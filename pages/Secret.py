import streamlit as st
from PIL import Image
import base64
import pickle
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from bokeh.models.widgets import Div
st.set_page_config(page_title = 'Movie recommandation system',
	               page_icon = 'Logo.png',layout = "centered"  )
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('secret.png')

st.image("Enjoy.gif", use_column_width=True)


df_ML =  pd.read_pickle('df_porn_ML.pkl')

st.title("Secret recommendation system")

movie  = st.multiselect("Choose a movie", df_ML, max_selections=1)

col1, col2, col3, col4, col5 = st.columns(5)
with col3 : 
    button2 =st.button("Dig in me")

if button2 : 
    col1, col2, col3, col4, col5 = st.columns(5)
    X = df_ML.drop(columns = ['Title', 'Year', 'Country', 'Poster', 'imdbID'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    distanceKNN = NearestNeighbors(n_neighbors=11).fit(X_scaled)
    neighbor = distanceKNN.kneighbors(X_scaled[df_ML['Title'] == movie[0]])
    
if button2 : 
    col1, col2, col3 = st.columns(3)    
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][0], 3])

if button2 : 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(df_ML.iloc[neighbor[1][0][1], 3])
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][2], 3])
    with col3:
        st.image(df_ML.iloc[neighbor[1][0][3], 3])
    with col4:
        st.image(df_ML.iloc[neighbor[1][0][4], 3])
    with col5:
        st.image(df_ML.iloc[neighbor[1][0][5], 3])
        
    col1, col2, col3, col4, col5 = st.columns(5)    

    with col1:
        st.markdown(df_ML.iloc[neighbor[1][0][1], 0])

    with col2:
        st.markdown(df_ML.iloc[neighbor[1][0][2], 0])

    with col3:
        st.markdown(df_ML.iloc[neighbor[1][0][3], 0])

    with col4:
        st.markdown(df_ML.iloc[neighbor[1][0][4], 0])

    with col5:
        st.markdown(df_ML.iloc[neighbor[1][0][5], 0])

if button2 :
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(df_ML.iloc[neighbor[1][0][6], 3])
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][7], 3])
    with col3:
        st.image(df_ML.iloc[neighbor[1][0][8], 3])
    with col4:
        st.image(df_ML.iloc[neighbor[1][0][9], 3])
    with col5:
        st.image(df_ML.iloc[neighbor[1][0][10], 3])

    col1, col2, col3, col4, col5 = st.columns(5)    

    with col1:
        st.markdown(df_ML.iloc[neighbor[1][0][6], 0])

    with col2:
        st.markdown(df_ML.iloc[neighbor[1][0][7], 0])

    with col3:
        st.markdown(df_ML.iloc[neighbor[1][0][8], 0])

    with col4:
        st.markdown(df_ML.iloc[neighbor[1][0][9], 0])

    with col5:
        st.markdown(df_ML.iloc[neighbor[1][0][10], 0])
