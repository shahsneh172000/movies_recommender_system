import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=92fa98bb1f8c379655c6879dc69a98c3&language=en-US'.format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommand(movie):
    movie_index = movies[movies['title']==movie].index[0]
    dist = similarity[movie_index]
    movie_list = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    rec_movies = []
    rec_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_poster.append(fetch_posters(movie_id))

    return rec_movies,rec_poster

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title("Movie Recommender System")

option = st.selectbox('How would you like to be contacted?',movies['title'].values)

# st.write('You selected:', option)
if st.button('Recommand'):
    names,posters = recommand(option) 
    # for i in ans:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


