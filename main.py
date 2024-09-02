import json
from unittest import result
import urllib.parse
from get_grid import get_lat_long,get_bounding_box
from dotenv import load_dotenv
import os
from send_requests import send_requests_using_proxy



headers= {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-form-factors": "\"Desktop\"",
    "sec-ch-ua-full-version": "\"128.0.6613.84\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"128.0.6613.84\", \"Not;A=Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"128.0.6613.84\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client-data": "CJS2yQEIprbJAQipncoBCKmJywEIkqHLAQiFoM0BCLKezgEIiaPOAQjlr84BCNq3zgEY9MnNARi+rs4BGJ2xzgEYmbzOAQ==",
    "x-goog-ext-353267353-jspb": "[null,null,null,147535]",
    "x-maps-diversion-context-bin": "CAE=",
    "Referer": "https://www.google.com/",
    "Referrer-Policy": "origin"
    }









def main():
    final_results=[]
    for  lat_long in lat_long_list:
        lat = lat_long[0]
        long = lat_long[1]
        for zoom in  zoom_levels:
            url = f"https://www.google.com/search?tbm=map&authuser=0&hl=en&pb=!4m12!1m3!1d{zoom}!2d{long}!3d{lat}!2m3!1f0!2f0!3f0!3m2!1i1517!2i674!4f13.1!7i{count}!8i{start}!10b1!12m20!1m2!18b1!30b1!2m3!5m1!6e2!20e3!10b1!12b1!13b1!16b1!17m1!3e1!20m3!5e2!6b1!14b1!46m1!1b0!94b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m5!1swIHQZpHzL4mC7M8P9JSx6Ao%3A79!2s1i%3A0%2Ct%3A150715%2Cp%3AwIHQZpHzL4mC7M8P9JSx6Ao%3A79!7e81!12e3!17swIHQZpHzL4mC7M8P9JSx6Ao%3A84!24m104!1m31!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m20!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!17b1!20b1!21b1!22b1!25b1!27m1!1b0!28b0!31b0!32b0!33m1!1b1!10m1!8e3!11m1!3e1!14m1!3b0!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m1!1b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m19!1m5!1b1!2b1!3b1!5b1!7b1!4b1!8m10!1m6!4m1!1e1!4m1!1e3!4m1!1e4!3sother_user_reviews!6m1!1e1!9b1!89b1!98m3!1b1!2b1!3b1!103b1!113b1!114m3!1b1!2m1!1b1!117b1!122m1!1b1!125b0!126b1!127b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i530!2i674!1m6!1m2!1i1467!2i0!2m2!1i1517!2i674!1m6!1m2!1i0!2i0!2m2!1i1517!2i20!1m6!1m2!1i0!2i654!2m2!1i1517!2i674!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!42b1!47m0!49m9!3b1!6m2!1b1!2b1!7m2!1e3!2b1!8b1!9b1!50m4!2e2!3m2!1b1!3b1!67m3!7b1!10b1!14b1!69i704&q={encoded_keyword}&nfpr=1&tch=1&ech=1&psi=wIHQZpHzL4mC7M8P9JSx6Ao.1724940746483.1"
            response = send_requests_using_proxy(url,headers,SCRAPEOPS_API_KEY)

            raw_input = response.text.replace('/*""*/',"")
            try:
                raw_input = json.loads(raw_input)["d"]
            except Exception as e:
                print(raw_input)

            prepared_data = prepare(raw_input)
            list_results = build_results(prepared_data)
            for result in list_results:
                if result not in final_results:
                    final_results.append(result)
    return final_results

def prepare(input):
    # Remove the first 5 characters and newlines
    prepared_for_parsing = input[4:].replace('\n', '')
    with open("prepared.txt","w",encoding="utf-8") as f:
        f.write(prepared_for_parsing)
    json_data = json.loads(prepared_for_parsing)
    results = []
    # results = [item[14] for item in json_data[0][1]]
    del json_data[0][1][0]
    for item in json_data[0][1]:
        try:
            results.append(item[14])
        except Exception as e:
            print(f"Error: {e}")
    return results

def prepare_lookup(data):
    # This function returns a lookup function for retrieving data using a list of indexes
    def lookup(*indexes):
        try:
            result = data
            for index in indexes:
                result = result[index]
            return result
        except (IndexError, TypeError):
            return None
    return lookup

def build_results(prepared_data):
    results = []
    for place in prepared_data:
        lookup = prepare_lookup(place)

        # Use the indexes below to extract certain pieces of data
        # or as a starting point of exploring the data response.
        result = {
            'address': {
                'street_address': lookup(183, 1, 2),
                'city': lookup(183, 1, 3),
                'zip': lookup(183, 1, 4),
                'state': lookup(183, 1, 5),
                'country_code': lookup(183, 1, 6),
            },
            'name': lookup(11),
            'tags': lookup(13),
            'notes': lookup(25, 15, 0, 2),
            'placeId': lookup(78),
            'phone': lookup(178, 0, 0),
            'coordinates': {
                'long': lookup(208, 0, 2),
                'lat': lookup(208, 0, 3)
            }
        }
        results.append(result)
    
    return results

if __name__=="__main__":
    # Load the API key from the .env file
    load_dotenv("credentials.env")
    GEO_CODING_API_KEY = os.getenv('geocoding_api')
    SCRAPEOPS_API_KEY = os.getenv('scrapeops_api')

    keyword = input("Enter The keyword you want to search for: ")
    place = input("Enter The place you want to search for: ")

    encoded_keyword =  urllib.parse.quote(keyword)
    start = 0
    count = 200
    zoom_levels = [35000,15000,7000,3000]
    bounding_box = get_bounding_box(place,GEO_CODING_API_KEY)
    grid_length = 1
    lat_long_list = get_lat_long(bounding_box,grid_length)
    result = main()
    with open("result.json","w",encoding="utf-8") as f:
        for item in result:
            f.write(json.dumps(item) + ",\n")