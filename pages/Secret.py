import streamlit as st
from PIL import Image
import base64
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

st.image("logosecret.png", use_column_width=True)
st.title("Secret recommandation system")
st.text_input("Movie Title",autocomplete=None)
st.multiselect(
    'Category',
    ['Milf', 'Teen', 'Mature', 'Gay','lesbian','Trans','Shaved','Hairy','BBC','Anal'])

col1, col2, col3, col4, col5 = st.columns(5)
with col3 : 
    button2 =st.button("Dig in me")