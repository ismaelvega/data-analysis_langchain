# Advanced CSV Explorer

A Streamlit app powered by LangChain that lets you chat with your CSV or Excel files using OpenAI’s GPT models.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)

   * [1. Clone the repository](#1-clone-the-repository)
   * [2. Create a virtual environment](#2-create-a-virtual-environment)
   * [3. Activate the virtual environment](#3-activate-the-virtual-environment)
   * [4. Install dependencies](#4-install-dependencies)
   * [5. Configure Streamlit secrets](#5-configure-streamlit-secrets)
3. [Running the App](#running-the-app)
4. [Usage](#usage)
5. [Troubleshooting](#troubleshooting)

---

## Prerequisites

* Python 3.10+ installed
* `git` installed
* OpenAI API key

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/data-analysis_langchain.git
cd data-analysis_langchain
```

### 2. Create a virtual environment

Create a fresh Python virtual environment:

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

* On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```
* On Windows (PowerShell):

  ```powershell
  .\\venv\\Scripts\\Activate.ps1
  ```

### 4. Install dependencies

Install all required Python packages from the snapshot file:

```bash
pip install --upgrade pip setuptools
pip install -r installed_packages.txt
```

> **Note:** If you haven’t generated `installed_packages.txt`, run:
>
> ```bash
> pip freeze > installed_packages.txt
> ```

### 5. Configure Streamlit secrets

Create a `.streamlit/secrets.toml` file for your OpenAI API key:

```bash
mkdir -p .streamlit
cat <<EOF > .streamlit/secrets.toml
openai_api_key = "sk-your-openai-key-here"
EOF
```

Streamlit will automatically load this file at runtime.

---

## Running the App

With the virtual environment active and your secrets configured, launch the Streamlit server:

```bash
streamlit run automated.py
```

You should see output like:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Open the Local URL in your browser to interact with the app.

---

## Usage

1. **Upload** a CSV or Excel file.
2. **Inspect** the first few rows and dataframe info.
3. **Ask** natural-language questions about your data.
4. **Receive** answers generated by the LangChain agent.

---

## Troubleshooting

* **`ModuleNotFoundError: No module named 'langchain'`**:
  Ensure you installed dependencies in the active venv:

  ```bash
  pip install langchain langchain-openai openai
  ```

* **Secrets not loading**:
  Verify `.streamlit/secrets.toml` exists and contains `openai_api_key = "..."`.

* **Rebuilding the venv**:
  If things get messy, delete and recreate:

  ```bash
  deactivate
  rm -rf venv
  python3 -m venv venv
  source venv/bin/activate
  pip install -r installed_packages.txt
  ```