from test_base import urls

def test_pages(selenium_client):
    for blueprint, pages in urls.items():
        for page in pages:
            selenium_client.get('http://127.0.0.1:5000' + blueprint + page)
            for entry in selenium_client.get_log('browser'):
                print(blueprint, page, entry)
                assert entry['level'] != 'SEVERE'
    