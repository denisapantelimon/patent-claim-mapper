from app.services.evidence_extractor import extract_evidence
from app.services.infringement_analyzer import analyze_infringement

def generate_claim_chart(product, claim_elements):

    chart = []

    for element in claim_elements:

        evidence = extract_evidence(
            product,
            element["text"]
        )

        analysis = analyze_infringement(
            element["text"],
            evidence
        )

        chart.append({
            "claim_element": element["text"],
            "evidence": evidence,
            "analysis": analysis["analysis"],
            "confidence": analysis["confidence"]
        })

    return chart