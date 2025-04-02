from tests.api.endpoints.base_endpoint import Endpoint
headers = {"Content-Type": "application/json"}

class UpdateTask(Endpoint):
    schema = {
        "title": "string",
        "description": "string",
        "completed": "boolean"
    }

    def update_task(self, payload, task_id):
        self.response = self.session.put(f"{self.url}/tasks/{task_id}", headers=headers, json=payload)
        self.response_json = self.response.json()
        print(self.response_json)

    def get_title(self):
        return self.get_data()['title']

    def get_id(self):
        return self.get_data()['id']

    def get_description(self):
        return self.get_data()['description']

    def check_completed(self):
        return self.get_data()['completed']

    def check_code(self):
        return self.response.status_code

    def check_error_message(self):
        return self.get_data()['error']