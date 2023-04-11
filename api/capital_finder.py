from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = f'https://restcountries.com/v3.1/name/{dic["country"]}?fullText=true'
            r = requests.get(url)
            data = r.json()
            for country_data in data:
                country = country_data["name"]["common"]
                capital = country_data["capital"][0]
            message = f'The capital of {country} is {capital}'

        else:
            message = "Give me a word to define please"


        # if "capital" in dic:
        #     url =
        #     r = requests.get(url)
        #     data = r.json()
        #     definitions = []
        #     for word_data in data:
        #         definition = word_data["meanings"][0]["definitions"][0]["definition"]
        #         definitions.append(definition)
        #     message = str(definitions)
        #
        # else:
        #     message = "Give me a word to define please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return