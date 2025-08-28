# 📰 Digital-Skeptic-AI-Assistant
## Fake News & Bias Detector (Hackathon Project)

This project is a Streamlit-based AI application that analyzes any online article or news story and generates a fact-checking style report using OPENAI's openai/gpt-oss-120b model via Groq (For fast infereces).

It is designed to help readers quickly evaluate the credibility, tone, claims, entities, and potential biases in an article, while also generating counter-arguments and verification questions.

## Project Demo

[DEMO](https://drive.google.com/file/d/1fQzfhwz0ZscBR6AK1QapCq6XhgoqGAzc/view?usp=sharing)

## ✨ Features
🔗 Fetch articles from any URL – simply paste the link.

🤖 AI-powered analysis using Groq’s openai/gpt-oss-120b model.

## 📑 Structured report generation:

Key Claims Extraction

Tone & Sentiment Analysis

Red Flags Detection (bias, exaggeration, misinformation cues)

Verification Questions (for fact-checking)

Entity Recognition (people, places, organizations, events)

Counter-arguments (alternative perspectives)

## 🎨 Streamlit Frontend with a clean, interactive UI.
💾 Download option – export the AI-generated report in Markdown (and extendable to PDF).

## 🛠️ Tech Stack
Frontend: Streamlit

LLM Backend: Groq (via LangChain integration)

Language Model Framework: LangChain

Environment Management: Python venv + .env for API keys

## 📂 Project Structure
```
Darvix-AI/
│
├── .env                       # Environment variable
├── app.py                     # Streamlit frontend
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
│
└── src/
    ├── prompts.py             # Prompts
    ├── fetch_article.py       # Extracts article text from URL
    ├── analyze_article.py     # LLM wrapper (LangChain + Groq)
    └── generate_report.py     # Orchestrates analysis & builds report
```

## 🚀 Setup & Installation
Follow these steps carefully to run the project locally:

1️⃣ Clone the Repository
```
git clone https://github.com/ratnesh134/Digital-Skeptic-AI-Assistant.git
cd Darvix-AI
```
2️⃣ Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Set Up Environment Variables

Create a .env file in the project root:
```
touch .env
```
Add your Groq API Key (get it from Groq Console):
```
GROQ_API_KEY=your_api_key_here
```
5️⃣ Run the Streamlit App
```
streamlit run app.py
```
Your browser will open automatically at: 👉 http://localhost:8501

## 🖥️ How It Works (Flow)
User Input → Paste an article/news URL in the Streamlit app.

Text Extraction → fetch_article.py uses Newspaper3k to scrape the article text.

AI Analysis → generate_report.py passes text into structured LangChain Groq prompts.

LLM Output → analyze_article.py runs Groq’s Llama model to produce responses for:

Claims

Tone

Red Flags

Verification Questions

Entities

Counter-Arguments

Report Generation → Combined into a well-formatted Markdown report.

Frontend Display → Streamlit shows results in collapsible sections + download option.

## 🎯 Use Cases
📰 Journalists – Quick bias detection & fact-checking support.

🎓 Students & Researchers – Understanding multiple perspectives on a topic.

👩‍💻 Developers – Learn how to integrate Groq with LangChain & Streamlit.

🔍 Fact-checkers – Identify misinformation or manipulative language.

📱 General Readers – Build media literacy by questioning claims.

## ⚡ Example Report Output

When analyzing a news article, you might get:

Claims:

The government announced a new policy on renewable energy.

Experts warn about possible economic downsides.

Tone:

Optimistic but slightly one-sided in favor of the policy.

Red Flags:

Over-reliance on government statements without citing independent experts.

Verification Questions:

What do independent environmental groups say?

Are there cost-benefit studies available?

Entities:

Government of India, Ministry of Renewable Energy, Tata Power.

Counter-Argument:

While the policy looks promising, critics argue implementation challenges and costs are being underplayed.

## 🔧 Troubleshooting
❌ Invalid API Key Error → Make sure .env contains the correct GROQ_API_KEY.

❌ Article fetch failed → Check if the site blocks scraping or try another URL.

❌ Dependencies issue → Run pip install --upgrade pip setuptools wheel.

## 🌟 Future Enhancements
Add PDF export for reports.

Improve UI with expanders and themes in Streamlit.

Support multi-article comparison (e.g., same story across news outlets).

Add knowledge graph visualization of entities.

## 👨‍💻 Contributors

Ratnesh Kumar
