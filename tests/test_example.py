from tests.test_base import check_pages, check_blueprints


@check_pages('/', '/home/index')
def test_pages(base_client):
    # do something
    base_client.post('/', data={})
    # the pages are tested (GET request: 200) afterwards by the
    # @check_pages decorator


@check_blueprints('/forms', '/ui')
def test_blueprints(base_client):
    # do something
    base_client.post('/', data={})
    # the blueprints are tested (GET request: 200) afterwards by the
    # @check_blueprints decorator
