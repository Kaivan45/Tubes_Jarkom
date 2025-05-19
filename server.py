import socket
import threading
import os

# Konfigurasi server
HOST = '192.162.4.43' 
PORT = 8080
WEB_ROOT = './www'  

# Fungsi menangani koneksi client
def handle_client(conn, addr):
    print(f"[+] Terhubung dengan {addr}")
    try:
        request = conn.recv(1024).decode()
        if not request:
            return

        # Ambil baris pertama dari HTTP request (GET /nama_file HTTP/1.1)
        request_line = request.splitlines()[0]
        print(f"[*] Request: {request_line}")

        parts = request_line.split()
        if len(parts) < 2 or parts[0] != 'GET':
            return

        file_path = parts[1].lstrip('/')
        if file_path == '':
            file_path = 'index.html'

        full_path = os.path.join(WEB_ROOT, file_path)

        if os.path.isfile(full_path):
            with open(full_path, 'rb') as f:
                body = f.read()
            header = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
            ).encode()
            conn.sendall(header + body)
        else:
            body = b"<h1>404 Not Found</h1>"
            header = (
                "HTTP/1.1 404 Not Found\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n\r\n"
            ).encode()
            conn.sendall(header + body)

    finally:
        conn.close()
        print(f"[-] Koneksi ditutup dari {addr}")

# Fungsi utama menjalankan server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[+] Server berjalan di {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[=] Jumlah koneksi aktif: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
