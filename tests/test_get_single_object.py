from HW27.endpoints.get_single_object_endpoint import GetObject


def test_get_item():
    get_obj = GetObject()
    get_obj.get_obj()
    get_obj.check_response_is_200()
    get_obj.validate_schema(get_obj.get_data())
    assert get_obj.get_id() == '7'