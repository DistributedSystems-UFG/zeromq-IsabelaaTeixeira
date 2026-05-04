import zmq

SERVER_IP = "172.31.48.33" 

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://{SERVER_IP}:12345") 

socket.send(b"Hello world")
message = socket.recv()
socket.send(b"STOP")
print(message.decode())