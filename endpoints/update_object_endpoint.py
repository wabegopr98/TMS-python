import requests
from HW27.endpoints.base_endpoint import Endpoint

class UpdateObj(Endpoint):

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

    def upd_obj(self, payload, id):
        self.response = requests.put(f'{self.url}/objects/{id}', json = payload)
        self.response_json = self.response.json()

    def get_name(self):
        return self.get_data()['name']