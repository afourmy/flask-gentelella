from os import remove
from os.path import abspath, dirname, join, pardir
from sys import dont_write_bytecode, path
from werkzeug.datastructures import ImmutableMultiDict
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

@pytest.fixture
def user_client():
    app = create_app()
    client = app.test_client()
    with app.app_context():
        create = ImmutableMultiDict([('username', 'cisco'), ('password', 'cisco'), ('create_account', '')])
        login = ImmutableMultiDict([('username', 'cisco'), ('password', 'cisco'), ('login', '')])
        client.post('/login', data=create)
        client.post('/login', data=login)
        yield client
    remove(join(path_source, 'database.db'))