import pytest

from rentomatic.response_objects import response_objects as res


@pytest.fixture
def response_value():
    return {"key": ["value1", "value2"]}


@pytest.fixture
def response_type():
    return "ResponseError"


@pytest.fixture
def response_message():
    return "This is a response error"


def test_response_success_is_true(response_value):
    assert bool(res.ResponseSuccess(response_value)) is True


def test_response_success_has_type_and_value(response_value):
    response = res.ResponseSuccess(response_value)

    assert response.type == res.ResponseSuccess.SUCCESS
    assert response.value == response_value


def test_response_failure_is_false(response_type, response_message):
    assert bool(res.ResponseFailure(response_type, response_message)) is False


def test_response_failure_has_type_and_message(
    response_type, response_message
):
    response = res.ResponseFailure(response_type, response_message)

    assert response.type == response_type
    assert response.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    response = res.ResponseFailure(response_type, response_message)

    assert response.value == {
        "type": response_type,
        "message": response_message,
    }
