import requests
import jsonschema

from HW27.endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"}
                },
                "required": ["year", "price", "CPU model", "Hard disk size"]
            }
        },
        "required": ["id", "name", "data"]
    }

    def get_obj(self):
        self.response = requests.get(f"{self.url}/objects/7")
        self.response_json = self.response.json()

    def get_id(self):
        return self.get_data()["id"]