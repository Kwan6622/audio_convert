import streamlit as st
from transcribe import transcribe_audio
from summarize import summarize_text
from dotenv import load_dotenv

load_dotenv()

st.title("Audio Convert - Transcribe and Summarize Audio")

uploaded_file = st.file_uploader("Upload audio file", type=[ "mp3" , "wav" ])

if uploaded_file is not None: 
    with open("temp_audio.mp3", "wb") as file:
        file.write(uploaded_file.read())

    if st.button("Process"):
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio("temp_audio.mp3")
        with st.spinner("Summarizing..."):
            summary = summarize_text(transcript)

        tab1, tab2 = st.tabs(["Transcript", "Summary"])
        with tab1:
            st.subheader("Transcript")
            st.write(transcript)

        with tab2:
            st.subheader("AI Summary:")
            st.write(summary)
            st.download_button("Download Summary", summary, file_name="summary.txt")
