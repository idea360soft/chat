import streamlit as st
import openai
from dotenv import load_dotenv
import os

import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Safety check if API key is missing
if not openai_api_key:
    st.error("Please set your OpenAI API Key in the .env file.")
    st.stop()

# Initialize OpenAI client for latest openai version
client = openai.OpenAI(api_key=openai_api_key)

# Streamlit UI
st.set_page_config(page_title="ChatGPT GPT-4", page_icon="🤖", layout="wide")

st.title("🤖 IDEA360CHAT")
st.write("Enter your query and click Generate to get response from IDEA360CHAT.")

# Prompt input box
prompt = st.text_area("Your Prompt", placeholder="Ask anything...", height=200)

# Generation parameters
max_tokens = st.slider("Max Tokens", 50, 2000, 500, step=50)
temperature = st.slider("Temperature", 0.0, 1.5, 1.0, step=0.1)

if st.button("Generate Response"):
    if not prompt.strip():
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=max_tokens,
                    temperature=temperature,
                )
                generated_text = response.choices[0].message.content
                st.success("Response:")
                st.markdown(generated_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")
