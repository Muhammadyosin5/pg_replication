from locust import HttpUser, task


class AppUser(HttpUser):

    # Endpoint
    @task
    def home_page(self):
        data = {
            "name": "salom"
        }
        # data = self.client.get(f"/create?name={data['name']}")
        self.client.get('/')
