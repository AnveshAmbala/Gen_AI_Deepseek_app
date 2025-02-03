import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
import re

# Custom CSS styling
st.markdown("""
<style>
    /* General Background and Font Styles */
    .main {
        background-color: #181818; /* Darker background for a sleek look */
        color: #f5f5f5; /* Lighter font for better contrast */
        font-family: 'Roboto', sans-serif; /* Modern and clean font */
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #1f1f1f;
        padding: 20px;
        border-right: 2px solid #ff6347; /* Adds a subtle line for separation */
    }

    /* Sidebar Header */
    .sidebar header h1 {
        color: #ff6347; /* Accent color for headers */
        font-size: 1.5rem;
    }

    /* Input Textarea */
    .stTextInput textarea {
        color: #f5f5f5 !important;
        background-color: #333333 !important; /* Dark background for input */
        border: 2px solid #ff6347; /* Accent border */
        border-radius: 8px;
        padding: 10px;
    }

    /* Selectbox */
    .stSelectbox div[data-baseweb="select"] {
        color: #f5f5f5 !important;
        background-color: #333333 !important;
        border-radius: 8px;
        border: 2px solid #ff6347; /* Accent border for select box */
    }

    .stSelectbox svg {
        fill: #ff6347 !important; /* Accent color for icons */
    }

    .stSelectbox option {
        background-color: #1a1a1a !important;
        color: #f5f5f5 !important;
    }

    /* Dropdown Listbox */
    div[role="listbox"] div {
        background-color: #333333 !important;
        color: #f5f5f5 !important;
        border-radius: 8px;
    }

    /* Loading Spinner */
    .stSpinner {
        color: #ff6347 !important; /* Accent spinner color */
    }

    /* Chat Styling */
    .st-chat-message {
        padding: 12px;
        border-radius: 10px;
        margin-bottom: 10px;
    }

    /* User Message Styling */
    .st-chat-message-user {
        background-color: #292929;
        color: #f5f5f5;
        align-self: flex-end;
    }

    /* AI Message Styling */
    .st-chat-message-ai {
        background-color: #444444;
        color: #f5f5f5;
        align-self: flex-start;
    }

    /* Title Styling */
    h1 {
        color: #ff6347; /* Accent color for title */
    }

    /* Caption Styling */
    .st-caption {
        color: #c0c0c0; /* Lighter caption color */
    }
</style>
""", unsafe_allow_html=True)


st.title("💡 Anvesh's AI Assistant")
st.caption("🤖 Your AI-Powered Coding Companion integrated with Deepseek r1 distilled model with 1.5b parameters with Smart Debugging")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    selected_model = st.selectbox(
        "Choose AI Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    st.divider()
    st.markdown("### Features")
    st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: flex-start; gap: 10px;">
        <div style="display: flex; align-items: center; color: black;">
            <span style="font-size: 1.5rem; color: #ff6347;">🧠</span>
            <span style="font-size: 1.1rem; margin-left: 10px; color: black;">Intelligent Code Suggestions</span>
        </div>
        <div style="display: flex; align-items: center; color: black;">
            <span style="font-size: 1.5rem; color: #ff6347;">🔍</span>
            <span style="font-size: 1.1rem; margin-left: 10px; color: black;">Debugging and Error Analysis</span>
        </div>
        <div style="display: flex; align-items: center; color: black;">
            <span style="font-size: 1.5rem; color: #ff6347;">📜</span>
            <span style="font-size: 1.1rem; margin-left: 10px; color: black;">Code Documentation & Best Practices</span>
        </div>
        <div style="display: flex; align-items: center; color: black;">
            <span style="font-size: 1.5rem; color: #ff6347;">🎯</span>
            <span style="font-size: 1.1rem; margin-left: 10px; color: black;">Optimized Solution Design</span>
        </div>
    </div>
""", unsafe_allow_html=True)


    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# Initialize AI engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a highly skilled AI coding assistant. Provide direct and precise coding solutions "
    "with strategic debugging hints and concise explanations. Do not include internal thoughts or reasoning "
    "like '<think>' statements. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "🚀 Hey there, I'm AI_Anvesh! , eady to assist you with coding, debugging, and more! What can I help you with today?"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Ask a coding question...")

def clean_response(response):
    """Remove <think> tags and content."""
    return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    response = processing_pipeline.invoke({})
    return clean_response(response)  # Clean the response to remove <think> tags

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Add user message to log
    st.session_state.message_log.append({"role": "user", "content": user_query})
    
    # Generate AI response
    with st.spinner("🤖 Thinking..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    
    # Add AI response to log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
    # Rerun to update chat display
    st.rerun()
