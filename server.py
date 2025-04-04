import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

# Set the directory to serve the HTML files
Handler.directory = "."

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
