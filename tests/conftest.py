from os import remove
from os.path import abspath, dirname, join, pardir
from pytest import fixture
from selenium import webdriver
from threading import Thread
from time import sleep
import sys

path_test = dirname(abspath(__file__))
path_parent = abspath(join(path_test, pardir))
path_app = join(path_parent, 'source')
if path_app not in sys.path:
    sys.path.append(path_app)

from app import create_app


@fixture
def base_client():
    app = create_app()
    yield app.test_client()
    remove(join(path_test, 'database.db'))


@fixture
def user_client():
    app = create_app()
    client = app.test_client()
    create = {'username': '', 'password': '', 'create_account': ''}
    login = {'username': '', 'password': '', 'login': ''}
    with app.app_context():
        client.post('/login', data=create)
        client.post('/login', data=login)
        yield client
    remove(join(path_test, 'database.db'))


# @fixture
# def selenium_client():
#     app = create_app()
#     client = webdriver.Chrome(join(path_test, 'chromedriver', 'chromedriver'))
#     app_context = app.app_context()
#     app_context.push()
#     Thread(target=app.run).start()
#     # give the server some time to start
#     sleep(5)
#     yield client
#     remove(join(path_test, 'database.db'))
