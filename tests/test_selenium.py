from tests.test_base import urls


# this test uses selenium to check, for all pages of gentelella, that there
# are no severe entry in chromium logs.
def test_selenium(selenium_client):
    for blueprint, pages in urls.items():
        for page in pages:
            selenium_client.get('http://127.0.0.1:5000' + blueprint + page)
            for entry in selenium_client.get_log('browser'):
                assert entry['level'] != 'SEVERE'
