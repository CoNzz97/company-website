import streamlit as st
import pandas

# Contact page
topics = pandas.read_csv("topics.csv", sep=",")
st.title("Contact us")
st.selectbox("What would you like to contact us about", options=topics)
st.text_area("hide this", label_visibility="hidden")
st.button("Send")