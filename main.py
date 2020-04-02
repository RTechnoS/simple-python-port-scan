import socket,threading

site = input('Input host : ')
def scanPort(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    result = s.connect_ex((host, port))
    if result == 0:
        print('Port {} open'.format(port))
    s.close()


for i in range (1,10000):
    t = threading.Thread(target=scanPort, args=(site, i))
    t.start()
   
    
print('Selesai')
