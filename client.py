import socket
import sys

def send_http_request(server_host, server_port, file_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((server_host, int(server_port)))
        except Exception as e:
            print(f"Gagal terhubung ke server: {e}")
            return

        # Format HTTP request
        request = f"GET {file_path} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
        client_socket.sendall(request.encode())

        response = b""
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            response += chunk

    print("=== RESPONSE DARI SERVER ===")
    print(response.decode('utf-8', errors='replace'))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_host> <server_port> <filename>")
        print("Contoh: python client.py 192.162.4.43 8080 /index.html")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    filename = sys.argv[3]

    send_http_request(host, port, filename)
