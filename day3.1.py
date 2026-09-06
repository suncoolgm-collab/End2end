import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
s.bind(('127.0.0.1', 8000))                                     
s.listen()
while True:
    conn, address = s.accept()   
    data= conn.recv(1024)        
    print(data.decode())
    conn.close()
    
    