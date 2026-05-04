import zmq, time

context = zmq.Context()         
socket = context.socket(zmq.PUB)
# * escuta em todas as interfaces da rede
socket.bind("tcp://*:12345")              

print("Publicador iniciado...")
while True:                    
    time.sleep(5)
    t = "TIME " + time.asctime()
    socket.send(t.encode())
    print(f"Publicado: {t}")