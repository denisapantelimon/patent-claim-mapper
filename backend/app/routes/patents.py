from fastapi import APIRouter, HTTPException

from app.services.patent_loader import load_patent
from app.services.claim_parser import parse_claims
from app.services.product_search import find_candidate_products
from app.services.claim_chart_generator import generate_claim_chart

router = APIRouter(
    prefix="/patents",
    tags=["patents"]
)

@router.post("/analyze")
async def analyze_patent(request: dict):

    patent_number = request.get("patent_number")

    patent = load_patent(patent_number)

    if not patent:
        raise HTTPException(
            status_code=404,
            detail="Patent not found"
        )

    parsed_claims = parse_claims(
        patent["claims"]
    )

    products = find_candidate_products(
        parsed_claims
    )

    results = []

    for product in products:

        claim_chart = generate_claim_chart(
            product,
            parsed_claims
        )

        results.append({
            "product_name": product["name"],
            "claim_chart": claim_chart
        })

    return {
        "patent": patent_number,
        "results": results
    }