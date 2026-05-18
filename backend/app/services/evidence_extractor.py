def extract_evidence(product, claim_element):

    return {
        "quote": (
            f"{product['name']} supports wireless charging"
        ),
        "source_url": "https://example.com",
        "source_title": product["name"]
    }