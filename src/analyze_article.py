import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Load .env variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client via LangChain
llm = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile",
    temperature=0
)

def run_llm(prompt: str, article_text: str) -> str:
    """
    Run a single prompt against Groq LLM using LangChain's interface.
    """
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant that performs skeptical, critical analysis of news articles."),
        ("human", "{prompt}\n\nARTICLE:\n{article_text}")
    ])

    chain = chat_prompt | llm
    response = chain.invoke({"prompt": prompt, "article_text": article_text})
    return response.content
