import streamlit as st
import base64
from pathlib import Path
from app_pages import pc_price_predictor
def _img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


def show():
    st.title("🎮 Welcome to PCBuddy!")
    st.write("PC buddy Predicts Gaming PC prices with an accuracy of over **80%!**")

    st.image(
        f"data:image/png;base64,{_img_to_base64(Path(__file__).resolve().parent.parent / 'images' / 'PC_setup.jpg')}",
        width= 600
    )

    if st.button("❇️ Start Predicting Your Custom Gaming PC Price Now!", use_container_width=True):
        st.session_state.page = "PC Price Predictor"

    st.write("Visit the About page to learn more about this application and its features.")

if __name__ == "__main__":
    show()