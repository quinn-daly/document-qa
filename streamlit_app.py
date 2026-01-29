import streamlit as st
from openai import OpenAI

# st.set_page_config MUST be first!
st.set_page_config(
    page_title="IST488 Labs", 
    page_icon=None, 
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None
)

# Add the folder path to your lab files
lab1 = st.Page('labs/lab1.py', title='Lab 1: Build a Streamlit Document Q&A app')
lab2 = st.Page('labs/lab2.py', title='Lab 2: Document Summarizer')

# Navigation and run
pg = st.navigation(pages=[lab1, lab2], position="sidebar", expanded=False)
pg.run()