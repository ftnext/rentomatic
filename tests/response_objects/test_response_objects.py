import pytest

from rentomatic.response_objects import response_objects as res


@pytest.fixture
def response_value():
    return {"key": ["value1", "value2"]}


def test_response_success_is_true(response_value):
    assert bool(res.ResponseSuccess(response_value)) is True
