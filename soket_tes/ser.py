# Echo server program
import socket

HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)
conn, addr = s.accept()
print 'Connected by', addr
data = "oreoresagi"
while 1:
    s.listen(2)
    conn, addr = s.accept()
    print 'Connected by', addr
    print "1"
    data2 = conn.recv(1024)
    print "2"
    conn.sendall(data)
    print "3"
    conn.sendall(data2)
conn.close()
