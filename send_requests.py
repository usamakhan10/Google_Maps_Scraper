import requests

def send_requests_using_proxy(url,headers,api_key_for_scrapeops):
    response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': api_key_for_scrapeops,
        'url': url, 
    },
    headers=headers
    )
    return response

      