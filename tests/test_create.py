from HW27.endpoints.create_object_endpoint import CreateObj
from HW27.payload.payload import valid_create_payload

def test_create_object():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate_schema(new_obj.get_data())
    assert new_obj.get_name() == "Apple MacBook Pro 11111"
    print(new_obj.get_data())

    #id ff808181932badb6019538b5d7361130