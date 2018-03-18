from test_base import urls


def test_pages(user_client):
    for blueprint, pages in urls.items():
        for page in pages:
            pass
            # selenium_client.get('http://127.0.0.1:5000' + blueprint + page)
            # for entry in selenium_client.get_log('browser'):
            #     print(entry, blueprint, page)
            #     assert entry['level'] != 'SEVERE'
