import pythoncom
import pyttsx3  # assuming you're using this for text-to-speech
import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from win32com.client import Dispatch



def speak(text):
    pythoncom.CoInitialize()  # Initialize COM
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(text)



model = pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))


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
	st.title(" Email (or) SMS Spam Detection Application")
	st.write("Build with Streamlit & Python")
	activites=["Classification"]
	choices=st.sidebar.selectbox("Select Activities",activites)
	if choices=="Classification":
		st.subheader("Classification")
		msg=st.text_input("Enter a text")
		if st.button("Process"):
			print(msg)
			print(type(msg))
			data=[msg]
			print(data)
			vec=cv.transform(data).toarray()
			result=model.predict(vec)
			if result[0]==0:
				st.success("This is Not A Spam  Jede prashanth")
				speak("This is Not A Spam  Jedey prashanth")
			else:
				st.error("This is A Spam  Jede prashanth")
				speak("This is A Spam  Jedey prashanth")
main()
