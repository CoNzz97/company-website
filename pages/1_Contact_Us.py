import streamlit as st
import pandas
import smtplib
import dotenv as env
import os

env.load_dotenv("B:\Coding\Python\EnviromentVariables\.env")

MY_EMAIL = os.getenv("gmail_email")
PASSWORD = os.getenv("gmail_password")
GMAIL_SMTP = "smtp.gmail.com"


def send_email(email, reason, message):
    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(MY_EMAIL, to_addrs="pythontesting100@myyahoo.com", msg=f"Subject:New Contact.\n\n "
                            f"From: {email}\n"
                            f"Contact Reason: {reason}\n"
                            f"Message: {message}")


# Contact page
topics = pandas.read_csv("topics.csv", sep=",")
st.title("Contact us")
with st.form(key="contact form"):
    user_email = st.text_input("Your email address")
    contact_reason = st.selectbox("What would you like to contact us about", options=topics, key="topic")
    user_message = st.text_area("hide this", label_visibility="hidden", key="message")
    submit_button = st.form_submit_button()
    if submit_button:
        send_email(user_email, contact_reason, user_message)
