# Anime-Analysis-Recommendation

Overview
This system is designed to analyze and recommend anime based on user preferences. It utilizes a combination of cosine similarity and TF-IDF vectorization to generate personalized recommendations.

Files
Streamlit.py: This file contains the code for the Streamlit app that allows users to input their preferences and receive recommendations.
Anime Analysis.ipynb: This file contains the code for the data analysis and feature engineering steps used to prepare the data for the recommendation system.

Model
The model used in this system is based on cosine similarity and TF-IDF vectorization. Here's a brief overview of how it works:
Data Preprocessing: The data is cleaned and preprocessed to remove any missing values or irrelevant information.
TF-IDF Vectorization: The text data is converted into TF-IDF vectors, which capture the importance of each word in the context of the entire text.
Cosine Similarity: The TF-IDF vectors are then used to calculate the cosine similarity between each anime and the user's preferences. This measures the similarity between the two based on the words they have in common.
Recommendation Generation: The anime with the highest cosine similarity score is selected as the recommended anime.

How to Use
Run the Streamlit app by executing the code in Streamlit.py.
Input your preferences by selecting an anime from the dropdown menu.
The app will generate a list of recommended anime based on your preferences.

