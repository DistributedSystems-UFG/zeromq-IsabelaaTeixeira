import zmq, time, pickle, sys

PRODUCER_IP = "172.31.48.33"

# permite definir o ID do worker pelo terminal (python worker.py 1)
worker_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1

context = zmq.Context()
socket = context.socket(zmq.PULL)      
socket.connect(f"tcp://{PRODUCER_IP}:12345") 

thisworker = format(worker_id, '03d')

print(f"Worker {thisworker} iniciado...")
while True:
    print("Worker " + thisworker + " wants work")    
    work = pickle.loads(socket.recv())
    print("Worker " + thisworker + " gets   " + format(work, '03d'))
    time.sleep(work)