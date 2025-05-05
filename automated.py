import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
import io


# 📌 OpenAI API key
api_key = "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"

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
            model="gpt-4o-mini-2024-07-18",
            api_key=api_key
        ),
        df,
        verbose=False,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        **{"allow_dangerous_code": True}
    )
    
    # Ask prompt
    prompt = st.text_input("💬 Ask a question about your data")
    
    if prompt:
        with st.spinner("Thinking..."):
            response = agent.invoke(prompt)
            st.success("✅ Answer:")
            st.markdown(f"> {response['output']}")
