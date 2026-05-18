from openai import OpenAI
from dotenv import load_dotenv

import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def parse_claims(claim_text: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
Break this patent claim into discrete claim elements.

Return valid JSON only.

Format:
{
  "elements": [
    {
      "element_id": "1a",
      "text": "..."
    }
  ]
}
"""
            },
            {
                "role": "user",
                "content": claim_text
            }
        ],
        response_format={"type": "json_object"}
    )

    content = response.choices[0].message.content

    parsed = json.loads(content)

    return parsed["elements"]