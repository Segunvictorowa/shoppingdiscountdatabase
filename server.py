from http.server import HTTPServer, BaseHTTPRequestHandler

# Create a server using HTTP
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        # Setting path for our website
        if self.path == '/':
            self.path = '/index.html'
        # checking whether we can access to webpage or not
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()

        # Write file to the path
        self.wfile.write(bytes(file_to_open, 'UTF-8'))

# Take the web port at the moment is 8080
httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()