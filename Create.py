import random

def create(n, r1, r2, r3):
  process_queue = []
  numberOfProcess = []
  rand_1 = int(n*r1/100)
  rand_2 = int(n*r2/100)
  rand_3 = int(n*r3/100)

  for i in range(n):
    numberOfProcess.append(int(i+1))

  for i in range(rand_1):
    process_queue.append([])
    k = random.randint(0, len(numberOfProcess)-1)
    process_queue[i].append('P'+ str(int(numberOfProcess[k])))
    process_queue[i].append(int(numberOfProcess[k]))
    numberOfProcess.remove(int(numberOfProcess[k]))
    process_queue[i].append(random.randint(2, 8))
  for i in range(rand_2):
    process_queue.append([])
    k = random.randint(0, len(numberOfProcess)-1)
    process_queue[i+rand_1].append('P'+ str(int(numberOfProcess[k])))
    process_queue[i+rand_1].append(int(numberOfProcess[k]))
    numberOfProcess.remove(int(numberOfProcess[k]))
    process_queue[i+rand_1].append(random.randint(20, 30))
  for i in range(rand_3):
    process_queue.append([])
    k = random.randint(0, len(numberOfProcess)-1)
    process_queue[i+rand_1+rand_2].append('P'+ str(int(numberOfProcess[k])))
    process_queue[i+rand_1+rand_2].append(int(numberOfProcess[k]))
    numberOfProcess.remove(int(numberOfProcess[k]))
    process_queue[i+rand_1+rand_2].append(random.randint(35, 40))
   
  return process_queue


