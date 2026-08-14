import streamlit as st
import pandas as pd
import pickle

# Set page config
st.set_page_config(page_title="Netflix Recommender Engine", layout="wide")

# Load model artifacts
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

# Recommendation logic function
def recommend(movie_title, top_n=5):
    try:
        idx = movies[movies['title'] == movie_title].index[0]
        sim_scores = list(enumerate(similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
        
        recommended_titles = []
        recommended_details = []
        for i in sim_scores:
            recommended_titles.append(movies.iloc[i[0]].title)
            recommended_details.append({
                "Type": movies.iloc[i[0]].type,
                "Genre": movies.iloc[i[0]].listed_in,
                "Description": movies.iloc[i[0]].description
            })
        return recommended_titles, recommended_details
    except IndexError:
        return [], []

# UI Layout
st.title("🎬 Netflix Content Recommendation Engine")
st.write("Select a movie or TV show to get instant recommendations based on genre, cast, and plot content.")

selected_movie = st.selectbox(
    "Choose or search a title:",
    movies['title'].values
)

num_recommendations = st.slider("Number of recommendations:", min_value=1, max_value=10, value=5)

if st.button("Predict / Recommend"):
    names, details = recommend(selected_movie, top_n=num_recommendations)
    if names:
        st.subheader(f"Recommendations for '{selected_movie}':")
        for i in range(len(names)):
            with st.expander(f"{i+1}. {names[i]} ({details[i]['Type']})"):
                st.write(f"**Genre:** {details[i]['Genre']}")
                st.write(f"**Plot:** {details[i]['Description']}")
    else:
        st.error("Title not found in dataset.")
