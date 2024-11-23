from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


class FirewallHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Parse the request path
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/tomcatwar.jsp':
            # Read the content length
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            # Parse the POST data
            post_params = urllib.parse.parse_qs(post_data)
            # Check for malicious parameter
            if 'class.module.classLoader.resources.context.parent.pipeline.first' in post_params:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b'Forbidden: Malicious request detected')
                return

        # If not malicious, proceed as normal
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Request processed successfully')


def run(server_class=HTTPServer, handler_class=FirewallHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run()