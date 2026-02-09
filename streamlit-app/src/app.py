import streamlit as st
from app_pages import home, pc_price_predictor, about

def main():
    st.set_page_config(page_title="PCBuddy")

    st.sidebar.title("💎 PCBuddy")
    st.sidebar.divider()
    if "page" not in st.session_state:
        st.session_state.page = "Home"


    if st.sidebar.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
    if st.sidebar.button("💻 PC Price Predictor", use_container_width=True):
        st.session_state.page = "PC Price Predictor"
    if st.sidebar.button("ℹ️ About", use_container_width=True):
        st.session_state.page = "About"

    page = st.session_state.page

    if page == "Home":
        home.show()
    elif page == "PC Price Predictor":
        pc_price_predictor.show()
    elif page == "About":
        about.show()

if __name__ == "__main__":
    main()
