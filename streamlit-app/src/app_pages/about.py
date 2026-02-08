import streamlit as st

def show():
    st.title("About This Application")
    st.write("""
    This Streamlit application is designed to provide users with a platform to predict PC prices based on various input parameters. 
    The application consists of three main pages:
    
    - **Home**: An introduction to the application and its features.
    - **PC Price Predictor**: A tool that allows users to input specifications and receive a predicted price for a PC.
    - **About**: Information about the application, its purpose, and the team behind it.
    
    We aim to provide an easy-to-use interface for users looking to understand PC pricing better and make informed purchasing decisions.
    """)

if __name__ == "__main__":
    show()