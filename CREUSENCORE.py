import streamlit as st
from PIL import Image
import base64
import pickle
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors


primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

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


df_ML =  pd.read_pickle('df_ML_poster.zip')


movie  = st.multiselect("", df_ML, max_selections=1)


col1, col2, col3 = st.columns(3)

with col1 : 
	weight_genre = st.slider('Genre', min_value=1, max_value=4, step=1, key='test')
	weight_year = st.slider('Year', min_value=1, max_value=4, step=1, key='test2')
	weight_popularity = st.slider('Popularity', min_value=1, max_value=4, step=1, key='test22')
with col2 : 
	weight_ratings = st.slider('Rating', min_value=1, max_value=4, step=1, key='test3',)
	weight_actor = st.slider('Actors', min_value=1, max_value=4, step=1, key='test4')
	weight_director = st.slider('Director', min_value=1, max_value=4, step=1, key='test44')
with col3 : 	
	weight_producer = st.slider('Producer', min_value=1, max_value=4, step=1, key='test5')
	st.slider('Awards', min_value=1, max_value=4, step=1, key='test6')
	st.slider('Country', min_value=1, max_value=4, step=1, key='test66')


col1, col2, col3, col4, col5 = st.columns(5)


with col3 : 
	button2 =st.button("Dig it up")

if button2 : 
	col1, col2, col3, col4, col5 = st.columns(5)
	X = df_ML.drop(columns = ['primaryTitle', 'Poster', 'tconst'])
	scaler = StandardScaler()
	X_scaled = scaler.fit_transform(X)
	X_scaled[:, 0] = X_scaled[:, 0]*(weight_year)
	X_scaled[:, 2] = X_scaled[:, 2]*(weight_ratings)
	X_scaled[:, 3] = X_scaled[:, 3]*(weight_popularity)
	X_scaled[:, 4:32] = X_scaled[:, 4:32]*(weight_genre)
	X_scaled[:, 32:2284] = X_scaled[:, 32:2284]*(weight_actor)
	X_scaled[:, 2284:3501] = X_scaled[:, 2284:3501]*(weight_director)
	X_scaled[:, 3501::] = X_scaled[:, 3501::]*(weight_producer)
	distanceKNN = NearestNeighbors(n_neighbors=6).fit(X_scaled)
	neighbor = distanceKNN.kneighbors(X_scaled[df_ML['primaryTitle'] == movie[0]])
	

if button2 : 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(df_ML.iloc[neighbor[1][0][1], 4432])
        st.markdown(df_ML.iloc[neighbor[1][0][1], 0])
    with col2:
        
        st.image(df_ML.iloc[neighbor[1][0][2], 4432])
        st.markdown(df_ML.iloc[neighbor[1][0][2], 0])
    with col3:
        
        st.image(df_ML.iloc[neighbor[1][0][3], 4432])
        st.markdown(df_ML.iloc[neighbor[1][0][3], 0])
    with col4:
        
        st.image(df_ML.iloc[neighbor[1][0][4], 4432])
        st.markdown(df_ML.iloc[neighbor[1][0][4], 0])
    with col5:
        
        st.image(df_ML.iloc[neighbor[1][0][5], 4432])
        st.markdown(df_ML.iloc[neighbor[1][0][5], 0])

