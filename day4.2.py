import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen()

while True:
    conn, address = s.accept()

    buffer = b""
    while True:
        chunk = conn.recv(1024)
        if chunk == b"":
            break
        buffer += chunk
        if b"\r\n\r\n" in buffer:
            break

    if b"\r\n\r\n" not in buffer:
        conn.close()
        continue

    head, body = buffer.split(b"\r\n\r\n", 1)

    content_length = 0
    lines = head.split(b"\r\n")
    line_0 = lines[0]
    for line in lines[1:]:                      
        name, sep, value = line.partition(b":")
        if name.strip().lower() == b"content-length":
            content_length = int(value.strip())
            break

    while len(body) < content_length:
        chunk = conn.recv(1024)
        if chunk == b"":                        
            break
        body += chunk
        
    method, path, ver= line_0.split(b" ", 2)

    respd_status="200 OK"
    
    if method == b"GET":
        respd_body= method
    elif method == b"POST":
        respd_body= path
    elif method == b"DELETE":
        respd_body= method+path
    else:
        respd_status="405 Method Not Allowed"
        respd_body = b"unsupported"
    respd=(
        b"HTTP/1.1 " +str(respd_status).encode() +b"\r\n"
        b"Content-Type: text/plain; charset=utf-8\r\n"
        b"Content-Length: "+str(len(respd_body)).encode()+b"\r\n"
        b"Connection: close\r\n\r\n"
        + respd_body
    )

    conn.sendall(respd)
            
    print(head.decode())
    print("---- body ----")
    print(body.decode())

    conn.close()
