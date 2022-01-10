import openai as ai
import os as os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

ai.api_key = os.getenv('OPENAI_API_KEY')

st.sidebar.title('Configurations')
st.header('This is an Explainer App')
st.subheader('This app uses OpenAI API to summarize text entered into the text box into a summary')
text_input = st.text_input('Enter your text here')
clicked_button  = st.button('click me') 
print(text_input)

if clicked_button:
    response = ai.Completion.create(engine="davinci", prompt=text_input, max_tokens=5)
    st.write(response.choices[0].text)
