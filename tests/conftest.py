import pytest

from rentomatic.app import create_app
from rentomatic.flask_settings import TestConfig


@pytest.fixture(scope="function")
def app():  # for pytest-flask
    return create_app(TestConfig)
