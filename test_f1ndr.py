from engines.f1ndr.f1ndr import f1ndr

def main():
    print("Running f1ndr test...\n")

    query = "mountain bike"
    result = f1ndr.search(query)

    print("Query:", query)
    print("Category:", result.get("category"))
    print("Platforms Used:", result.get("platforms_used"))
    print("Total Results:", result.get("total_results"))
    print("\nFirst Result:\n", result["results"][0] if result["results"] else "No results")

if __name__ == "__main__":
    main()
