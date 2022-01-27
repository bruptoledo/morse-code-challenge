import pytest
from back.app import create_app


@pytest.fixture(scope="session")
def app(request):
    app = create_app()
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(request, app):
    client = app.test_client()
    return client
