# f1ndr_backend/tests/load/load_test_locust.py

from locust import HttpUser, task, between

API_KEY = "dev-key"  # replace with your real key


class F1NDRLoadUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def search_load_test(self):
        self.client.post(
            "/search",
            headers={"X-API-Key": API_KEY},
            json={"query": "mountain bike", "radius_km": 100, "limit": 20},
        )
