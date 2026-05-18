import json
from pathlib import Path

DATA_PATH = Path("app/data/PatentData.json")


def load_patent(patent_number: str):
    with open(DATA_PATH, "r") as f:
        patents = json.load(f)

    for patent in patents:
        if patent["patent_number"] == patent_number:
            return patent

    return None