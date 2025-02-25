from HW27.endpoints.get_all_objects_endpoint import GetAllObject


def test_get_all_item():
    get_all_obj = GetAllObject()
    get_all_obj.get_obj()
    get_all_obj.check_response_is_200()
    get_all_obj.validate_schema(get_all_obj.get_data())
    assert get_all_obj.get_data() #проверили что нам приходит не пустой ответ