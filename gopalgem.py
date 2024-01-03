import streamlit as st
import google.generativeai as palm  # For generating game reviews
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

def main():
    st.header("Game Review Wizard ")
    st.write("")

    game_name = st.text_input("Enter the name of the game you want to review:")

    if st.button("Get Review", use_container_width=True):
        model = "models/text-bison-001"  # Replace with a suitable game review model

        prompt = f"Write a comprehensive review of the game {game_name}, covering its gameplay, graphics, story, and overall experience."
        response = palm.generate_text(
            model=model,
            prompt=prompt,
            max_output_tokens=1024
        )

        st.write("")
        st.header(":blue[Game Review]")
        st.write("")

        st.markdown(response.result, unsafe_allow_html=False, help=None)

if _name_ == "_main_":
    main()