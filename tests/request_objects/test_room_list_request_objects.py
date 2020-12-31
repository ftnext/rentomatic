from rentomatic.request_objects import room_list_request_object as req


def test_build_room_list_request_object_without_parameters():
    request = req.RoomListRequestObject()

    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_object_from_empty_dict():
    request = req.RoomListRequestObject.from_dict({})

    assert request.filters is None
    assert bool(request) is True


def test_build_room_list_request_object_with_empty_filters():
    request = req.RoomListRequestObject(filters={})

    assert request.filters == {}
    assert bool(request) is True


def test_build_room_list_request_object_from_dict_with_empty_filters():
    request = req.RoomListRequestObject.from_dict({"filters": {}})

    assert request.filters == {}
    assert bool(request) is True


def test_build_room_list_request_object_from_dict_with_filters_wrong():
    request = req.RoomListRequestObject.from_dict({"filters": {"a": 1}})

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "filters"
    assert bool(request) is False
