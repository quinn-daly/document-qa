import streamlit as st
from openai import OpenAI

pg = st.navigation(pages = [lab1, lab2], position="sidebar", expanded=False)
st.set_page_config(page_title="IST488 Labs", page_icon=None, layout="wide", initial_sidebar_state="expanded", menu_items=None)
pg.run()

lab1 = st.Page('lab1.py', title='Lab 1: Build a Streamlit Document Q&A app')
lab2 = st.Page('lab2.py', title='Lab 2: Document Summarizer')

