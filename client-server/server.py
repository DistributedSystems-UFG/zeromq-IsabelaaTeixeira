import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
# * permite que o servidor escute conexões externas
socket.bind("tcp://*:12345") 

print("Servidor aguardando requisições...")
while True:
    message = socket.recv()
    if not "STOP" in str(message):
        reply = str(message.decode()) + '*'
        socket.send(reply.encode())
    else:
        break