import streamlit as st
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
import os

genai.configure(api_key="AIzaSyDV4WzJV0KQlCAk1cwf1fqC5wW_i4WAyM4")

# Streamlit UI setup
st.set_page_config(page_title="Conversational AI Data Science Tutor", layout="centered")
st.title("🤖 Conversational AI Data Science Tutor")
st.write("Ask any data science-related questions, and I'll assist you!")

# Initialize memory for conversation awareness
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# User Input
user_query = st.text_input("💬 Ask a Data Science Question:")

if st.button("Send"):
    if user_query:
        with st.spinner("Thinking..."):
            # Retrieve conversation history
            conversation_history = st.session_state.memory.load_memory_variables({})["history"]
            
            prompt = f"""
            Act as a Data Science tutor. Maintain context from previous discussions.
            
            **Conversation History:**
            {conversation_history}
            
            **Current Question:** {user_query}
            
            Provide an explanation, examples, and references to common data science concepts where necessary.
            """
            
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-002")
            response = model.generate_content(prompt)
            
            # Store user query and response in memory
            st.session_state.memory.save_context({"input": user_query}, {"output": response.text})
            
            st.success("✅ AI Response:")
            st.markdown(response.text)
    else:
        st.warning("⚠️ Please enter a question.")
