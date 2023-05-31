import streamlit as st
import pandas

# Home page
st.set_page_config(layout="wide", page_title="The Best Company")
st.title("The Best Company")
content1 = """Welcome to the official website of the esteemed Best Company, where excellence meets innovation. Since 
our establishment in 1990, right at the onset of the dynamic tech boom, we have consistently been at the forefront of 
the industry. With our expertise in Data, App, and Website creation, as well as LLM and AI science, we have made a 
significant impact on the digital landscape.

Our team of highly skilled professionals, equipped with a deep understanding of cutting-edge technologies, 
strives to deliver exceptional results. From talented developers and designers to data scientists and AI experts, 
each member of our team plays a crucial role in our success. We take pride in fostering a collaborative and inclusive 
work environment that encourages creativity, problem-solving, and continuous learning.

Thank you for visiting our website. We invite you to explore and experience the world of Best Company. Together, 
let's create extraordinary digital solutions and embark on a journey towards success and innovation."""
st.write(content1)
st.divider()
st.header("Our Team")
col1, emp_col1, col2, emp_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])

st.divider()





