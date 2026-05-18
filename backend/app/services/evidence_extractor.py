import trafilatura

def extract_evidence(product, claim_element):

    url = product.get("url")

    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return {
            "quote": "No evidence found",
            "source_url": url,
            "source_title": product["name"]
        }

    text = trafilatura.extract(downloaded)

    if not text:
        text = ""

    shortened = text[:2000]

    return {
        "quote": shortened,
        "source_url": url,
        "source_title": product["name"]
    }