import streamlit as st
import sf

st.title("Lights, camera, action!")
genre = st.sidebar.selectbox("Genre", ("Adventure", "Comedy", "Sci-Fi", "Horror"))

if genre:
    response = sf.generate_movie_details(genre)
    st.header(response['movie_title'])

    st.write("**Plot**")
    st.write(response['plot'])

    cast_list = response['cast'].split(",")
    st.write("**Suggested Cast**")
    for actor in cast_list:
        st.write("-", actor)
