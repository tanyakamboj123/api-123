import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()

        names = self.parse_query_parameters()
        marks = {"marks": [10, 20]}  # Example marks
        self.wfile.write(json.dumps(marks).encode('utf-8'))

    def parse_query_parameters(self):
        query = self.path.split('?')[-1]
        query_dict = {}
        if query:
            for param in query.split('&'):
                key, value = param.split('=')
                query_dict[key] = value
        return query_dict.get('name', [])
