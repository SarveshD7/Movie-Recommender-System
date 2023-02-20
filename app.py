import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommend_movies = []
    movies_list2 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list2:
        movie_id = i[0]
        # fetch poster from api

        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


similarity = pickle.load(open('similarity.pkl','rb'))
movies_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)
movies_list = movies_list['title'].values
st.title('Movie Recommender System')
selectedMovieName = st.selectbox('Select a Movie',movies_list)


if st.button('Recommend'):
    recommendations = recommend(selectedMovieName)
    for i in recommendations:
        st.write(i)

