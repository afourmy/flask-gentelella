from os import remove
from os.path import abspath, dirname, join, pardir
from pytest import fixture
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from threading import Thread
# from time import sleep
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
#     app = create_app(True)
#     app_context = app.app_context()
#     app_context.push()
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     # Flask can run in a separate thread, but the reloader expects to run in
#     # the main thread: it must be disabled
#     Thread(
#         target=app.run,
#         kwargs={
#             'host': '0.0.0.0',
#             'port': 5000,
#             'use_reloader': False
#         }
#     ).start()
#     # give the server some time to start
#     sleep(1)
#     client = webdriver.Chrome(
#         join(path_test, 'chromedriver', 'chromedriver.exe'),
#         chrome_options=options
#     )
#     yield client
#     client.get('http://127.0.0.1:5000/shutdown')
#     client.quit()
#     app_context.pop()
#     remove(join(path_test, 'database.db'))
