# src/prompts.py

PROMPT_CLAIMS = """
Extract 3–5 main factual claims made in the article. 
Only include claims that could, in principle, be independently verified. 
Avoid opinions or speculation. 
Return the output as a bulleted list.
"""

PROMPT_TONE = """
Analyze the language and tone of the article. 
Classify whether it appears neutral, persuasive, emotional, or strongly opinionated. 
Provide a short explanation and cite at least two words or phrases from the article that support your classification.
"""

PROMPT_RED_FLAGS = """
Identify potential red flags in this article’s reporting. 
Examples include: use of loaded terminology, reliance on anonymous sources, lack of cited data, 
absence of opposing viewpoints, or one-sided framing. 
Return the output as a bulleted list.
"""

PROMPT_QUESTIONS = """
Generate 3–4 specific questions a critical reader should ask to independently verify this article’s content. 
Each question should be concrete and actionable, not generic.
Return the output as a numbered list.
"""

PROMPT_ENTITIES = """
Identify the key entities mentioned in the article (people, organizations, institutions, and locations). 
For each entity, suggest one thing a critical reader should investigate about them (e.g., background, funding, prior credibility).
Return the output as a bulleted list in the format:
- Entity Name: Suggested investigation
"""

PROMPT_COUNTER = """
Summarize this article from the perspective of someone who disagrees with its main claims. 
Do not misrepresent the article, but highlight how the narrative might be framed differently from an opposing viewpoint.
Keep the summary concise (3–5 sentences).
"""
