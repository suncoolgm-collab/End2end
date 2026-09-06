import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8000))
s.listen()

while True:
    conn, address = s.accept()

    # 1) \r\n\r\n 나올 때까지 받는다
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

    # 2) 버퍼를 헤더 부분과 그 뒤로 나눈다
    head, body = buffer.split(b"\r\n\r\n", 1)

    # 3) 헤더에서 Content-Length 값을 찾는다
    content_length = 0
    lines = head.split(b"\r\n")
    for line in lines[1:]:                      # lines[0]은 요청 라인(GET / HTTP/1.1)
        name, sep, value = line.partition(b":")
        if name.strip().lower() == b"content-length":
            content_length = int(value.strip())
            break

    # 4) 그 뒤에 이미 들어온 바이트가 몇 개인지 센다  ->  len(body)
    # 5) 부족한 만큼 recv를 더 부른다
    while len(body) < content_length:
        chunk = conn.recv(1024)
        if chunk == b"":                        # 클라이언트가 중간에 끊음
            break
        body += chunk

    print(head.decode())
    print("---- body ----")
    print(body.decode())

    conn.close()
