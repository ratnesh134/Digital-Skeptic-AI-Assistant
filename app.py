import streamlit as st
from src.fetch_article import fetch_article_text
from src.generate_report import generate_report

st.set_page_config(page_title="Digital Skeptic AI", layout="wide")

st.title("📰 Digital Skeptic AI")
st.markdown("Empowering Critical Thinking in an Age of Information Overload")

url = st.text_input("Enter the URL of a news article:")

if st.button("Analyze Article") and url:
    with st.spinner("Fetching and analyzing article..."):
        article = fetch_article_text(url)
        report = generate_report(article)
    
    st.markdown(report)
    # Option to download
    st.download_button("Download Report", report, file_name="critical_analysis_report.md")
