from HW27.endpoints.create_object_endpoint import CreateObj
from HW27.endpoints.delete_object_endpoint import DeleteObject
from HW27.payload.payload import valid_create_payload


def test_delete_object():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate_schema(new_obj.get_data())
    obj_for_del = new_obj.get_id()
    del_obj = DeleteObject()
    del_obj.del_obj(obj_for_del)
    del_obj.check_response_is_200()
    del_obj.validate_schema(del_obj.get_data())
    assert del_obj.get_message() == f"Object with id = {obj_for_del} has been deleted."