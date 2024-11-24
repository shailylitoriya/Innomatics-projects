import streamlit as st
import google.generativeai as genai
import datetime
import time

#key setup
genai.configure(api_key='AIzaSyAbJoY_3hKTDByJsnd3xQuEDHwNdBWwClg')
# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")
# System Prompt
sys_prompt = """
You are An AI Code Reviewer, an expert AI Python Code Reviewer. Review and Analyze submitted Python code and provide:
1. ## 🐞 Bug Report: Identify potential bugs, syntax errors and logical flaws in the code. Provide concise explanations for each issue in the form of a clear, numbered list.
2. ## 🛠️ Fixed Code: Provide corrected or optimized code snippets, along with explanations of the changes made.
3. ## 💡 Code Insights: Offer clear, concise, and helpful feedback suitable for developers with various levels of experience; in the form of a clear, numbered list.  
Keep the tone professional and the explanations straightforward, aiming for clarity, accuracy, and enhancing the user's understanding of good coding practices.
"""
# Function - To get response
def get_response(sys_prompt, code_input):
    response = model.generate_content([sys_prompt, code_input])
    return response.text
#frontend part
# Set up the page configuration
st.set_page_config(
    page_title="An AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)
# Page Header
#st.title("🤖 AlphaBot: Your Python Code Reviewer")
st.markdown("<h1 style='text-align: center;'>🤖 <span style='color: Blue;'>Code Reviewer</span></h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Get your Python code analyzed and optimized by AI</h3>", unsafe_allow_html=True)

#if st.session_state.page == "Home":
 # Intro
st.markdown("---")
st.write("### Analyze your Python code, fix bugs, and gain insights!")
st.markdown("Welcome to **Code Reviewer**, your personal AI-powered code reviewer! Paste your Python code below and Code Reviewer will do the rest.")
    
# Input Section
st.write("#### 📝 Code Input")
code_input = st.text_area("Enter your Python code here: ", placeholder="Enter your Python code")

# Review button
review_button = st.button("Review Code")
response = get_response(sys_prompt, code_input)
st.write(response)

