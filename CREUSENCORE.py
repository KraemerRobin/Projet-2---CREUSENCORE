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


st.set_page_config(page_title = 'Movie recommendation system',
	               page_icon = 'Logo.png',layout = "centered",initial_sidebar_state = "collapsed"  )
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
add_bg_from_local("test3black.png")

st.image("logo.gif", use_column_width=True)


df_ML =  pd.read_pickle('df_main_final.zip')


movie  = st.multiselect("", df_ML, max_selections=1)


col1, col2, col3 = st.columns(3)

with col1 : 
    weight_year = st.slider('Year', min_value=1, max_value=10, step=1, key='test2')
    
with col2 : 
    weight_actor = st.slider('Actors', min_value=1, max_value=50, step=1, key='test4')
    
with col3 : 	
    weight_director = st.slider('Director', min_value=1, max_value=10, step=1, key='test44')





col1, col2, col3, col4, col5 = st.columns(5)


with col3 : 
	button2 =st.button("Dig it up")

if button2 : 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        with st.spinner('Digging...'):

            X = df_ML.drop(columns = ['french_title', 'Poster', 'tconst'])
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            X_scaled[:, 0] = X_scaled[:, 0]*(weight_year)
            X_scaled[:, 2] = X_scaled[:, 2]*60
            X_scaled[:, 3] = X_scaled[:, 3]*16
            X_scaled[:, 4:28] = X_scaled[:, 4:28]*74
            X_scaled[:, 28:163] = X_scaled[:, 28:163]
            X_scaled[:, 163:1589] = X_scaled[:, 163:1589]*(weight_actor)
            X_scaled[:, 1589:] = X_scaled[:, 1589:]*(weight_director)*3
            distanceKNN = NearestNeighbors(n_neighbors=11).fit(X_scaled)
            neighbor = distanceKNN.kneighbors(X_scaled[df_ML['french_title'] == movie[0]])



if button2 : 
    col1, col2, col3 = st.columns(3)    
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][0], 6])

if button2 : 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(df_ML.iloc[neighbor[1][0][1], 6])
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][2], 6])
    with col3:
        st.image(df_ML.iloc[neighbor[1][0][3], 6])
    with col4:
        st.image(df_ML.iloc[neighbor[1][0][4], 6])
    with col5:
        st.image(df_ML.iloc[neighbor[1][0][5], 6])
        
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
        st.image(df_ML.iloc[neighbor[1][0][6], 6])
    with col2:
        st.image(df_ML.iloc[neighbor[1][0][7], 6])
    with col3:
        st.image(df_ML.iloc[neighbor[1][0][8], 6])
    with col4:
        st.image(df_ML.iloc[neighbor[1][0][9], 6])
    with col5:
        st.image(df_ML.iloc[neighbor[1][0][10], 6])

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
