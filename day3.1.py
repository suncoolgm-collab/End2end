import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen()

def handle(conn, address):
    conn.settimeout(2)
    buffer = b""
    while True:
        try:
            chunk = conn.recv(1024)
        except socket.timeout:
            break
        if chunk == b"":
            break

        buffer += chunk

        if b"\r\n\r\n" in buffer:
            break

    if b"\r\n\r\n" not in buffer:
        conn.close()
        return
    print(buffer.decode())
    respd = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        "Content-Length: 5\r\n"
        "Connection: close\r\n\r\n"
        "hello"
        )
    conn.sendall(respd.encode())
    conn.close()

while True:
    conn, address = s.accept()
    threading.Thread(target=handle, args=(conn, address)).start()
