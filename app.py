import streamlit as st
import google.generativeai as genai

# Streamlit UI Setup
st.title("📝 Text Generator using Google Gemini AI")

# Input for API Key
api_key = st.text_input("Enter your Google Gemini API Key", type="password")

# Input for user prompt
user_prompt = st.text_area("Enter a prompt for text generation")

# Button to generate text
if st.button("Generate Text"):
    if not api_key:
        st.error("Please enter a valid API Key.")
    elif not user_prompt:
        st.error("Please enter a prompt.")
    else:
        # Configure Gemini AI with the provided API Key
        genai.configure(api_key=api_key)

        # Generate the text response
        try:
            model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" for text tasks
            response = model.generate_content(user_prompt)

            # Display the response
            if response.text:
                st.subheader("Generated Response:")
                st.write(response.text)
            else:
                st.error("No response generated. Try a different prompt.")
        
        except Exception as e:
            st.error(f"Error: {e}")
