import streamlit as st
import google.generativeai as genai
import os
import time

def get_api_key():
    """Retrieves the API key from a file securely."""
    key_file_path = os.path.join("keys", "gemini.txt")
    try:
        with open(key_file_path, "r") as file:
            api_key = file.read().strip()  # Read and remove any trailing whitespace
            return api_key
    except FileNotFoundError:
        raise Exception(f"API key file not found at {key_file_path}. Please ensure it exists.")

# Load the API key securely
api_key = get_api_key()
genai.configure(api_key=api_key)  # Set the API key using the library's configuration

# Initialize the Generative AI model (Gemini)
sys_prompt = """You are an expert, helpful, and sensible AI Python Code Reviewer. User will give you Python code, and you should analyze it to identify any bugs or errors.

There are three possible scenarios for the code you receive: incorrect code, correct code, or irrelevant content.

If you receive incorrect code, organize your response into three sections:

Bug Report: Mention the name of the error, the corresponding erroneous part of the code, and a brief description of the error.
Corrected Code: Provide the corrected code with proper comments."""

# to do the code reviewing task, we need the help of an LLM
# here, we have chosen gemini-1.5-flash model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                          system_instruction=sys_prompt)

# giving a title to the app's UI
# Displaying the title
st.title(":red[AI Code Reviewer]")

# Create columns for centering the image
col1, col2, col3 = st.columns([1, 3, 1])  # Create three columns, center image in the middle column
with col2:
    # Display the image with custom width and smaller size
    st.image("ai.png", caption="AI Code Reviewer", width=300)



# enabling a simple UI for user to enter or paste their code
st.markdown('<p style="font-size: 20px; color: white;"><b>Enter your Python code below:</b></p>', unsafe_allow_html=True)
# ask the user to enter their code & collect it in the variable 'user_prompt'
user_prompt = st.text_area("", placeholder="Type or paste your code here...")
# displaying a button to the user to submit the code
st.markdown("""
    <style>
    .stButton>button {
        background-color: white;
        color: black;
        font-weight: bold;
        width: 200px;
        height: 50px;
        border-radius: 10px;
        margin: auto;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# displaying a button to the user to submit the code
btn_click_1 = st.button("Submit")
# suppose the user clicks the button, the following need to be done
if btn_click_1==True:
    # display a message to the user
    with st.spinner(':blue_book: Analyzing your code:hourglass:!'):
        time.sleep(7)
        # ask the model to generate response from the user_prompt
        response = model.generate_content(user_prompt)
        # display the response
        st.markdown(response.text, unsafe_allow_html=True)
