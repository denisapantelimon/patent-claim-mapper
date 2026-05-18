from ddgs import DDGS

def find_candidate_products(parsed_claims):

    search_queries = []

    for claim in parsed_claims:
        search_queries.append(claim["text"])

    results = []

    with DDGS() as ddgs:

        for query in search_queries[:3]:

            search_results = ddgs.text(
                query,
                max_results=5
            )

            for item in search_results:

                results.append({
                    "name": item.get("title"),
                    "url": item.get("href"),
                    "snippet": item.get("body")
                })

    return results