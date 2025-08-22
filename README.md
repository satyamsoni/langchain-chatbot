# Lang Chain Sample
Learn LangChain LLM Implementation

## Purpose : 
Setup Chatbot

## How to setup 
1. Clone the repo "git clone git@github.com:satyamsoni/langchain-llm.git"
2. Run Setup file "./setup.sh" after giving execute permission.

source venv/bin/activate

## How to Try on CLI
run "python LLM.py prompt_message"

## How to try on Browser
### Load Chatbot API
uvicorn server:app --reload
### Run Chatbot Server
python3 -m http.server 8080
### Run on Browser
open index.html