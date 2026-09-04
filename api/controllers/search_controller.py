from api.utils.string_utils import safe_lower, safe_strip
from api.utils.pagination import paginate_results
from api.utils.id_generator import generate_id
from api.utils.response_builder import success_response

class SearchController:
    """
    Controller for search operations.
    Thin layer: validate → use utils → respond.
    """

    def search(self, query: str, page: int = 1, per_page: int = 20):
        normalized = safe_lower(safe_strip(query))

        # Dummy results for now — replace with your real engine later
        results = [
            {
                "id": generate_id(),
                "title": f"Result for '{normalized}' #{i+1}",
                "source": "placeholder"
            }
            for i in range(50)
        ]

        paginated = paginate_results(results, page, per_page)

        return success_response(
            data=paginated,
            message="Search results"
        )
