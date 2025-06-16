import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get your OpenAI API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Safety check if API key is missing
if not openai_api_key:
    st.error("Please set your OpenAI API Key in the .env file.")
    st.stop()

# Set the API key
openai.api_key = openai_api_key

# Streamlit page configuration
st.set_page_config(page_title="ChatGPT GPT-4", page_icon="🤖", layout="wide")

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333333;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            font-size: 18px !important;
        }
        .stButton>button {
            font-size: 20px !important;
            background-color: #1a73e8;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stMarkdown {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🤖 IDEA360AIGPT")
st.write("Enter your query and click Generate to get response from IDEA360AIGPT .")

# Prompt input box
prompt = st.text_area("Your Prompt", placeholder="Ask anything...", height=200)

# Generation parameters (optional sliders)
max_tokens = st.slider("Max Tokens", 50, 2000, 500, step=50)
temperature = st.slider("Temperature", 0.0, 1.5, 1.0, step=0.1)

# Generate button
if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o",  # Using GPT-4o model
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                generated_text = response['choices'][0]['message']['content']
                st.success("Response:")
                st.markdown(generated_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
