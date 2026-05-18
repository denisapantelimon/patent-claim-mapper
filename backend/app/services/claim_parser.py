def parse_claims(claim_text: str):

    parts = claim_text.split(";")

    elements = []

    for idx, part in enumerate(parts):

        elements.append({
            "element_id": f"1{chr(97 + idx)}",
            "text": part.strip()
        })

    return elements