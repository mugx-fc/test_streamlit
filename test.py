import streamlit as st

login_form = st.form("login_form")
login_form.title("Login")
login_form.text_input("Email", placeholder="your_email@email.com")
login_form.text_input("Password")
login_form.form_submit_button("Login")
