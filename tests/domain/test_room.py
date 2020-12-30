import uuid

from rentomatic.domain import room as r


def test_room_model_init():
    code = uuid.uuid4()

    room = r.Room(
        code, size=200, price=10, longitude=-0.09998975, latitude=51.75436293
    )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_from_dict():
    code = uuid.uuid4()

    room = r.Room.from_dict(
        {
            "code": code,
            "size": 230,
            "price": 11,
            "longitude": -0.09398975,
            "latitude": 58.75436293,
        }
    )

    assert room.code == code
    assert room.size == 230
    assert room.price == 11
    assert room.longitude == -0.09398975
    assert room.latitude == 58.75436293


def test_room_model_to_dict():
    room_dict = {
        "code": uuid.uuid4(),
        "size": 300,
        "price": 17,
        "longitude": -0.09899975,
        "latitude": 55.71436293,
    }
    room = r.Room.from_dict(room_dict)

    assert room.to_dict() == room_dict
