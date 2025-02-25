from HW27.endpoints.update_object_endpoint import UpdateObj
from HW27.payload.payload import valid_update_payload
from HW27.payload.payload import valid_create_payload
from HW27.endpoints.create_object_endpoint import CreateObj


def test_update_item():
    new_obj = CreateObj()
    new_obj.new_obj(valid_create_payload)
    new_obj.check_response_is_200()
    new_obj.validate_schema(new_obj.get_data())
    obj_for_upd = new_obj.get_id()
    upd_obj = UpdateObj()
    upd_obj.upd_obj(valid_update_payload, obj_for_upd)
    upd_obj.check_response_is_200()
    upd_obj.validate_schema(upd_obj.get_data())
    assert upd_obj.get_name() == "Apple MacBook Pro 16"

