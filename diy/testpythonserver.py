import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

working_dir = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) > 1:
	working_dir = sys.argv[1]

# set working directory
os.chdir(working_dir)

def run(host, port=8080):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
	host = os.environ.get('OPENSHIFT_DIY_IP')
	port = os.environ.get('OPENSHIFT_DIY_PORT', '8080')
	port = int(port)

	run(host, port)
