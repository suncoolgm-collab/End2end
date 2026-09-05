import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(('127.0.0.1', 8000))                                     
s.listen()
while True:
    conn, address = s.accept()   
    buffer = b""
    while True:
        chunk= conn.recv(1024)
        if chunk==b"":
            break
        
        buffer+=chunk
        
        if b"\r\n\r\n" in buffer:
            break
    
    if b"\r\n\r\n" not in buffer:
        conn.close()
        continue        
    print(buffer.decode())   
    respd=(
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        "Content-Length: 5\r\n\r\n"
        "hello"
        )
    conn.sendall(respd.encode())
    conn.close()
