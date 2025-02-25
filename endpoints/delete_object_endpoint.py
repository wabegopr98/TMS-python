import requests
import jsonschema

from HW27.endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"}

        },
        "required": ["message"]
    }


    def del_obj(self, my_id):
        self.response = requests.delete(f"{self.url}/objects/{my_id}")
        self.response_json = self.response.json()

    def get_message(self):
        return self.get_data()['message']