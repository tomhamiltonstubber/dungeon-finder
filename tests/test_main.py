from tests.conftest import test_client


def test_index():
    r = test_client.get('/')
    assert 'Hello World' in r.content.decode()
