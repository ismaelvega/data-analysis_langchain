import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import io

# ui enhancements
from IPython.display import Markdown, display
import contextlib

# 📌 OpenAI API key
api_key = st.secrets["openai_api_key"]

# Page config
st.set_page_config(page_title="Advanced CSV Explorer", layout="wide")
st.title("📊 Chat With Your File – Powered by Langchain & Magic")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload your CSV or Excel file", type=["csv", "xlsx"])


if uploaded_file:
    # Detect file type and read accordingly
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    
    st.dataframe(df.head())
    
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    # Create agent with hardcoded API key
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(
            temperature=0,
            model="gpt-4.1-2025-04-14",
            api_key=api_key
        ),
        df,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        **{"allow_dangerous_code": True}
    )
    def display_clean_output(agent, prompt):
        buffer = io.StringIO()

        # stdout'u geçici olarak yönlendiriyoruz (böylece zincir mesajları bastırılıyor)
        with contextlib.redirect_stdout(buffer):
            result = agent.invoke(prompt)

        # Sadece temiz 'output' kısmını gösteriyoruz
        output = result.get("output", "").strip()
        st.markdown(output)


    # Ask prompt
    prompt = st.text_input("💬 Ask a question about your data")

    if prompt:
        with st.spinner("Thinking..."):
            # Display the clean output
            display_clean_output(agent, prompt)
