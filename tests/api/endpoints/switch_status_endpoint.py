from tests.api.endpoints.base_endpoint import Endpoint
headers = {"Content-Type": "application/json"}

class SwitchStatusTask(Endpoint):
    schema = {

        "completed": "boolean",
        "created_at": "datetime",
        "description": "string",
        "id": "integer",
        "title": "string",
        "user_id": "integer"
    }

    def switch_status_task(self, task_id):
        self.response = self.session.post(f"{self.url}/tasks/{task_id}/toggle", headers=headers)
        self.response_json = self.response.json()
        print(self.response_json)

    def get_id(self):
        return self.get_data()['id']

    def check_completed(self):
        return self.get_data()['completed']

    def check_code(self):
        return self.response.status_code
