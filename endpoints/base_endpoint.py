import jsonschema
from HW27 import settings


class Endpoint:
    response = None
    response_json = None
    schema = {}
    url = settings.url

    def check_response_is_200(self):
        assert self.response.status_code == 200, f'{self.response.status_code}'

    def check_response_is_400(self):
        assert self.response.status_code == 400, f'{self.response.status_code}'

    def validate_schema(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def get_data(self):
        return self.response.json()