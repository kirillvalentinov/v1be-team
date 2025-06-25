import socket
import http.server
import socketserver
import webbrowser
from contextlib import closing

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
        return port

def run_server():
    port = find_free_port()
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Сервер запущен на порту {port}")
            print(f"Откройте в браузере: http://localhost:{port}/crossword.html")
            webbrowser.open(f'http://localhost:{port}/crossword.html')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        httpd.server_close()

if __name__ == '__main__':
    run_server() 