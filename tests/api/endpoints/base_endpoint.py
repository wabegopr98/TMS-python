import jsonschema
import requests
from tests import settings
default_session = requests.Session()

class Endpoint:
    response = None
    response_json = None
    schema = {}
    session = default_session
    url = settings.url

    def validate_schema(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def get_data(self):
        return self.response.json()