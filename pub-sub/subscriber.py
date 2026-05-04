import zmq

PUB_IP = "172.31.48.33"

context = zmq.Context()
socket = context.socket(zmq.SUB)          
socket.connect(f"tcp://{PUB_IP}:12345")   
socket.setsockopt(zmq.SUBSCRIBE, b"TIME") 

for i in range(5):
    time_msg = socket.recv()
    print(time_msg.decode())