from HW27.conftest import first_item
from HW27.endpoints.get_list_objects_by_id_endpoint import GetListObject


def test_get_list_item():
    get_ls_obj = GetListObject()
    get_ls_obj.get_obj()
    get_ls_obj.check_response_is_200()
    get_ls_obj.validate_schema(get_ls_obj.get_data())
    assert get_ls_obj.get_item_first_name() == first_item