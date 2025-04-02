from tests.api.endpoints.base_endpoint import Endpoint
headers = {"Content-Type": "application/json"}

class CreateTask(Endpoint):
    schema = {
        "type":"object",
        "propeties": {
        "title": "string",
        "description": "string",
        "completed": "boolean"
    },
    "required": ["title"]
    }


    def create_task(self, payload):
        self.response = self.session.post(f"{self.url}/tasks", headers = headers, json=payload)
        self.response_json = self.response.json()
        print(self.response_json)

    def get_title(self):
        return self.get_data()['title']

    def check_completed(self):
        return self.get_data()['completed']

    def get_code(self):
        return self.response.status_code

    def get_description(self):
        return self.get_data()['description']

    def get_id(self):
        return self.get_data()['id']
