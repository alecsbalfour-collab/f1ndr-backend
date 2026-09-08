# test_f1ndr.py
# End-to-end API test for F1NDR backend

import httpx

BASE_URL = "http://localhost:8000"
API_KEY = "dev-key"  # or your real key

def main():
    print("Running F1NDR API test...\n")

    query = "mountain bike"

    response = httpx.post(
        f"{BASE_URL}/search",
        headers={"X-API-Key": API_KEY},
        json={"query": query, "radius_km": 50, "limit": 10},
    )

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Error:", response.text)
        return

    result = response.json()

    print("Query:", query)
    print("Total Results:", result.get("total_results"))
    print("Platforms Used:", result.get("platforms_used"))

    first = result["results"][0] if result.get("results") else None
    print("\nFirst Result:\n", first or "No results")

if __name__ == "__main__":
    main()
