import streamlit as st
from transformers import pipeline

st.title("Text Summarizer with LLM")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

user_input = st.text_area("Enter text to summarize", height=200)
if st.button("Summarize"):
    summary = summarizer(user_input, max_length=50, min_length=20, do_sample=False)
    st.subheader("Summary")
    st.write(summary[0]['summary_text'])
