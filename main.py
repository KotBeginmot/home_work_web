from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"
server_port = 8080


class server(BaseHTTPRequestHandler):
    """Класс для возвращения GET запроса"""

    def __get_content(self):
        with open('web_list.html', 'r', encoding='utf-8') as file:
            return file.read()

    def do_GET(self):
        page_content = self.__get_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), server)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")