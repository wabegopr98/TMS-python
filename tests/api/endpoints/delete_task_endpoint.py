from tests.api.endpoints.base_endpoint import Endpoint
headers = {"Content-Type": "application/json"}

class DeleteTask(Endpoint):

    def delete_task(self, task_id):
        self.response = self.session.delete(f"{self.url}/tasks/{task_id}", headers=headers)
#        self.response_json = self.response.json()
#        print(self.response_json)

    def check_code(self):
        return self.response.status_code