from tests.api.endpoints.base_endpoint import Endpoint


class GetTask(Endpoint):
    schema = {

        "completed": "boolean",
        "created_at": "datetime",
        "description": "string",
        "id": "integer",
        "title": "string",
        "user_id": "integer"
    }

    def get_task(self, task_id):
        self.response = self.session.get(f"{self.url}/tasks/{task_id}")
        self.response_json = self.response.json()
        print(self.response_json)

    def get_title(self):
        return self.get_data()['title']

    def get_id(self):
        return self.get_data()['id']

    def get_code(self):
        return self.response.status_code