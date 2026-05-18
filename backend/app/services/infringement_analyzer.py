from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def analyze_infringement(claim_element, evidence):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
Analyze whether the evidence matches
the patent claim element.

Only use explicit evidence.
"""
            },
            {
                "role": "user",
                "content": f"""
Claim Element:
{claim_element}

Evidence:
{evidence['quote']}
"""
            }
        ]
    )

    analysis = response.choices[0].message.content

    return {
        "analysis": analysis,
        "confidence": 0.75
    }