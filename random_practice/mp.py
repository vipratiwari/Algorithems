from multiprocessing import Process
import os
import math

def calc():
    for i in range(1, 5000000):
        math.sqrt(i)
        
processes = []

for p in range(os.cpu_count()):
    print(" Registering Procecss %d "%p)
    processes.append(Process(target=calc))
    
for p in processes:
    p.start()
    
for p in processes:
    p.join()
