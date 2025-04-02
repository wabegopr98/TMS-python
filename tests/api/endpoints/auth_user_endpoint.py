from tests.api.endpoints.base_endpoint import Endpoint
headers = {"Content-Type": "application/json"}

class AuthUser(Endpoint):
    schema = {
        "username": "string",
        "password": "string"
    }

    def login_user(self, payload):
        self.response = self.session.post(f"{self.url}/login", json=payload, headers = headers)
        self.response_json = self.response.json()
        print(self.response_json)

    def get_message(self):
        return self.get_data()['message']

    def get_error(self):
        return self.get_data()['error']

    def get_code(self):
        return self.response.status_code

    def get_username(self):
        return self.get_data()['username']