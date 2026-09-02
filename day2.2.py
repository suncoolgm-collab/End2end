from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello, 안녕".encode("utf-8"))

def run(server_class=HTTPServer,handler_class=BaseHTTPRequestHandler):
    server_address=('', 8000)
    httpd=server_class(server_address,handler_class)
    httpd.serve_forever()
    
run(handler_class=SimpleHandler)
print(0)