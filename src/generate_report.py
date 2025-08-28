# src/generate_report.py

from src.analyze_article import run_llm
from src.prompts import (
    PROMPT_CLAIMS,
    PROMPT_TONE,
    PROMPT_RED_FLAGS,
    PROMPT_QUESTIONS,
    PROMPT_ENTITIES,
    PROMPT_COUNTER
)

def generate_report(article: dict) -> str:
    """
    Generate a markdown critical analysis report for a given article.
    Article dict must have keys: title, text.
    """

    sections = {}

    # Run prompts one by one
    sections["claims"] = run_llm(PROMPT_CLAIMS, article["text"])
    sections["tone"] = run_llm(PROMPT_TONE, article["text"])
    sections["red_flags"] = run_llm(PROMPT_RED_FLAGS, article["text"])
    sections["questions"] = run_llm(PROMPT_QUESTIONS, article["text"])
    sections["entities"] = run_llm(PROMPT_ENTITIES, article["text"])
    sections["counter"] = run_llm(PROMPT_COUNTER, article["text"])

    # Assemble Markdown report
    markdown_report = f"""
# Critical Analysis Report for: {article.get('title', 'Unknown Title')}

### Core Claims
{sections['claims']}

### Language & Tone Analysis
{sections['tone']}

### Potential Red Flags
{sections['red_flags']}

### Verification Questions
{sections['questions']}

---

### 🔎 Bonus Features
**Key Entities to Investigate:**
{sections['entities']}

**Counter-Argument Simulation:**
{sections['counter']}
"""

    return markdown_report
