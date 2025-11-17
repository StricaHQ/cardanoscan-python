# tests/conftest.py
import pytest
from cardanoscan import Cardanoscan

@pytest.fixture
def client():
    c = Cardanoscan(api_key="mock-api-key")
    yield c
    c.close()