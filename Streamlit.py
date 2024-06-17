import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import requests
from io import BytesIO
import os

# Set page width
st.set_page_config(layout="wide")

cosine_sim = pickle.load(open('cosine_sim.pkl','rb'))
indices = pickle.load(open('indices.pkl','rb'))

# Function that takes in anime title as input and outputs most similar animes
def get_recommendations(name, cosine_sim=cosine_sim):
    # Get the index of the anime that matches the title
    for i in range(len(indices)):
        if name==indices[i][1]:
            idx=i

    # Get the pairwsie similarity scores of all animes with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the animes based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar animes
    sim_scores = sim_scores[1:11]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar animes
    return anime_new['name'].iloc[anime_indices], anime_new['image_url'].iloc[anime_indices], anime_new['synopsis'].iloc[anime_indices], anime_new['score'].iloc[anime_indices], anime_new['rating'].iloc[anime_indices] 

# Function to filter anime dataset based on selected anime
def filter_anime(selected_anime):
    return anime_new[anime_new['name'] == selected_anime]
    
# Load the anime dataset
anime_new = pd.read_csv('anime_new.csv')

# Create a Streamlit app
st.title('Anime Search')

# Get unique anime names for dropdown
anime_list = anime_new['name'].values
selected_anime = st.selectbox(
    "Type or select an anime from the dropdown",
    anime_list)


# Display anime information if an anime is selected
if selected_anime:
    st.header('Anime Results')
    name, image_url, synopsis, score, rating = get_recommendations(selected_anime)
    for i in range(len(name)):
        st.subheader(name.iloc[i])
        col1, col2 = st.columns([1, 4])
        with col1:    
            try:
                # Attempt to fetch and resize the image from URL
                response = requests.get(image_url.iloc[i])
                img = Image.open(BytesIO(response.content))
                img_resized = img.resize((210, 310))
                st.image(img_resized, use_column_width=False)
            except Exception as e:
                img_local = Image.open('error.jpg')
                img_resized = img_local.resize((210, 310))
                st.image(img_resized, use_column_width=False)   
        with col2:
            st.write(f"**Score:** {score.iloc[i]}")
            st.write(f"**Rating:** {rating.iloc[i]}")
            st.write("**Synopsis:**")
            # st.write(synopsis.iloc[i])  # Display synopsis as paragraph
            st.markdown(f"<p style='text-align: justify;'>{synopsis.iloc[i]}</p>", unsafe_allow_html=True)  # Justify synopsis text

