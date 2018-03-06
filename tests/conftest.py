from os import remove
from os.path import abspath, dirname, join, pardir
from sys import dont_write_bytecode, path
import pytest
import tempfile

path_source = dirname(abspath(__file__))
path_parent = abspath(join(path_source, pardir))
path_app = join(path_parent, 'source')
if path_app not in path:
    path.append(path_app)

from app import create_app

@pytest.fixture
def base_client():
    app = create_app()
    yield app.test_client()
    remove(join(path_source, 'database.db'))

# credentials = 

@pytest.fixture
def user_client():
    app = create_app()
    client = app.test_client()
    create = {'username': '', 'password': '', 'create_account': ''}
    login = {'username': '', 'password': '', 'login': ''}
    with app.app_context():
        client.post('/login', data=create)
        client.post('/login', data=login)
        yield client
    remove(join(path_source, 'database.db'))
