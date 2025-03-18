# Conversational AI Data Science Tutor

## Overview
This is an AI-powered chatbot designed to assist users with **data science-related queries**. The chatbot maintains **conversation memory** to provide context-aware responses, ensuring a smooth and interactive learning experience.

## Features
- ✅ **Conversation Awareness**: Remembers previous discussions for better responses.
- ✅ **Powered by Gemini 1.5 Pro**: Uses Google's **Gemini AI** for intelligent and relevant answers.
- ✅ **Streamlit UI**: User-friendly chat interface.
- ✅ **Real-time AI Responses**: Provides explanations, examples, and references for data science concepts.

## Technologies Used
- **Programming Language**: Python
- **Frameworks**: Streamlit, LangChain
- **AI Model**: Google Gemini 1.5 Pro

## Installation
### **1. Clone the Repository**
```bash
 git clone https://github.com/your-repo/conversational-ai-tutor.git
 cd conversational-ai-tutor
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up Your API Key**
Ensure you have a **Google GenAI API Key** and set it up as an environment variable:
```bash
export GOOGLE_GENAI_API_KEY="your-api-key-here"
```
For Windows (PowerShell):
```powershell
$env:GOOGLE_GENAI_API_KEY="your-api-key-here"
```

## Running the Application
Run the following command to start the chatbot:
```bash
streamlit run app.py
```

## How to Use
1. Enter your **data science-related question** in the chatbox.
2. Click **"Send"** to get a response.
3. The chatbot will remember your previous messages and continue the conversation accordingly.

## License
This project is licensed under the MIT License.

## Contact
For any issues or feature requests, feel free to raise an issue on GitHub!
