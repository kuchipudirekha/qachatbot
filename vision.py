# # Q&A Chatbot

import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(prompt, image=None):
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    if image and prompt:
        response = model.generate_content([prompt, image])
    elif image:
        response = model.generate_content(image)
    else:
        response = model.generate_content(prompt)
    return response.text

st.title("Free-tier Gemini Vision Chatbot")

prompt = st.text_input("Enter prompt:")
uploaded_file = st.file_uploader("Upload image (optional)", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image")

if st.button("Generate Response"):
    if not prompt and not image:
        st.error("Please enter a prompt or upload an image.")
    else:
        output = get_gemini_response(prompt, image)
        st.subheader("Response:")
        st.write(output)
