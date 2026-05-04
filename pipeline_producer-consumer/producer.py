import zmq, time, pickle, random

NWORKERS = 10

context = zmq.Context()              
socket = context.socket(zmq.PUSH)      

socket.bind("tcp://*:12345")    

print("Produtor iniciado...")
while True:
    workload = random.randint(1, 100)
    print("Produced workload", format(workload, '03d'))
    socket.send(pickle.dumps(workload))
    time.sleep(workload / NWORKERS)