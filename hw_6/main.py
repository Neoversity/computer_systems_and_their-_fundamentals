import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Виведемо шлях, який використовує сервер
        print(f"Serving from directory: {os.path.join(os.getcwd(), 'hw_6')}")
        self.directory = os.path.join(os.getcwd(), 'hw_6')
        
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/message.html':
            self.path = '/message.html'
        else:
            self.path = '/error.html'
        
        return SimpleHTTPRequestHandler.do_GET(self)

def run(server_class=HTTPServer, handler_class=MyHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
