from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>return "Version 3 - Git Working!"</h1>")

server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Server running on port 5000...")
server.serve_forever()
