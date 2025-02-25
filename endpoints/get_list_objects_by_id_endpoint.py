import requests
import jsonschema

from HW27.endpoints.base_endpoint import Endpoint


class GetListObject(Endpoint):

    schema = {
        "type": "array",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "color": {"type": "string"},
                    "price": {"type": "number"},
                    "capacity GB": {"type": "number"},
                    "Capacity": {"type": "string"},
                    "Screen size": {"type": "number"}
                },
            }
        },
        "required": ["id", "name", "data"]
    }

    def get_obj(self):
        self.response = requests.get(f"{self.url}/objects?id=3&id=5&id=10")
        self.response_json = self.response.json()

    def get_item_first_name(self):
        return self.get_data()[0]