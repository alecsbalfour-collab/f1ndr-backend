def paginate_results(results: list, page: int = 1, per_page: int = 20):
    """
    Simple pagination helper for list-based results.
    """
    start = (page - 1) * per_page
    end = start + per_page

    return {
        "page": page,
        "per_page": per_page,
        "total": len(results),
        "results": results[start:end]
    }
