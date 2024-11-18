# AI Code Reviewer App

This is a simple Streamlit app that utilizes Google Gemini AI to review Python code. Users can input their code directly into the app, and the AI model analyzes the code to identify any errors or bugs.

## Features

- **Python Code Review:** Users can input their Python code and get a comprehensive review.
- **Generative AI Integration:** The app uses Google Gemini's AI model to analyze code and provide suggestions.
- **User-Friendly UI:** The app allows users to easily interact with the interface and get feedback on their code.

## Setup Instructions

1. **Install Dependencies:**
   - Install Python and required libraries:
     ```bash
     pip install streamlit google-generativeai
     ```
2. **API Key Setup:**
   - The app requires an API key for the Google Gemini AI model.
   - Place your API key in a file named `gemini.txt` inside a folder called `keys`.

3. **Run the App:**
   - Once the dependencies are installed and the API key is set up, run the app using:
     ```bash
     streamlit run app.py
     ```
