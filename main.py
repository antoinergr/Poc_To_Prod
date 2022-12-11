import streamlit as st

from predict.predict import run

st.markdown('# Welcome on Tags Guesser')

text = st.text_input(
    label="text",
    placeholder="Enter the comment",
    label_visibility="hidden",
)


