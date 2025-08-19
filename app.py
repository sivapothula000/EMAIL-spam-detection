import platform
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from gtts import gTTS
import os

# Load model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

def speak(text):
    """Generates and plays speech audio in Streamlit."""
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    audio_file = open("output.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")

def main():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: skyblue;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Email / SMS Spam Detection Application")
    st.write("Built with Streamlit & Python")

    activities = ["Classification"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Classification":
        st.subheader("Enter your message below")
        msg = st.text_input("Enter a text")

        if st.button("Process"):
            data = [msg]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)

            if result[0] == 0:
                output = "This is Not a Spam, siva anand"
                st.success(output)
                speak(output)
            else:
                output = "This is a Spam, siva anand"
                st.error(output)
                speak(output)

if __name__ == "__main__":
    main()

