from HW27.endpoints.base_endpoint import Endpoint
import requests

class GetAllObject(Endpoint):
    schema = {
        "type": "array",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "color": {"type": "string"},
                    "capacity": {"type": "string"}
                },
            }
        },
        "required": ["id", "name", "data"]
    }

    def get_obj(self):
        self.response = requests.get(f"{self.url}/objects")
        self.response_json = self.response.json()