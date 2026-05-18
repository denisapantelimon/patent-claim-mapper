from pydantic import BaseModel
from typing import List, Optional


class PatentRequest(BaseModel):
    patent_number: str


class ClaimElement(BaseModel):
    element_id: str
    text: str


class Evidence(BaseModel):
    quote: str
    source_url: str
    source_title: str


class ClaimChartEntry(BaseModel):
    claim_element: str
    evidence: Evidence
    analysis: str
    confidence: float


class ProductAnalysis(BaseModel):
    product_name: str
    claim_chart: List[ClaimChartEntry]