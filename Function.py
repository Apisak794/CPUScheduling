def FCFS(Process, n):
  total_wtime = 0
  wtime = 0
  twt = []
  Process.sort(key = lambda Process:Process[1])
  burstt = []
  for i in range (len(Process)):
    burstt.append(Process[i][2])
  print(burstt)
  print(' ')
  for i in range(len(Process)-1):
    wtime += Process[i][2]
    twt.append(wtime)
  # print('ProcessName\tArrivalTime\tBurstTime')
  # for i in range(len(Process)):
  #   print(Process[i][0],'\t\t',Process[i][1],'\t\t',Process[i][2])
  for i in range (len(twt)):
    total_wtime += twt[i]

  print('Total waiting time: ',total_wtime)
  print('Average waiting time: ',(total_wtime/n))

def SJF(Process, n):
  total_wtime = 0
  wtime = 0
  twt = []
  Process.sort(key = lambda Process:Process[2])
  burstt = []
  for i in range (len(Process)):
    burstt.append(Process[i][2])
  print(burstt)
  print(' ')
  for i in range(len(Process)-1):
    wtime += Process[i][2]
    twt.append(wtime)
  # print('ProcessName\tArrivalTime\tBurstTime')
  # for i in range(len(Process)):
  #   print(Process[i][0],'\t\t',Process[i][1],'\t\t',Process[i][2])
  for i in range (len(twt)):
    total_wtime += twt[i]

  print('Total waiting time: ',total_wtime)
  print('Average waiting time: ',(total_wtime/n))

def RR(Process, n, qt):
  total_wtime = 0
  wtime = [0]
  twt = []
  cpProcess = []
  for i in range(len(Process)):
    cpProcess.append(Process[i][2])

  Process.sort(key = lambda Process:Process[1])
  
  while len(Process) > 0:
    newprocess = []
    burstt = []
    for i in range (len(Process)):
        burstt.append(Process[i][2])
    print(burstt)
    print(' ')
    # print(wtime)
    # print('ProcessName\tArrivalTime\tBurstTime')
    # for i in range(len(Process)):
    #   print(Process[i][0],'\t\t',Process[i][1],'\t\t',Process[i][2])
    # print(' ')
    # print('---------------------------------------------------')
    for i in range(len(Process)):
      if (Process[i][2] > qt):
          wtime.append(int(qt)+wtime[-1])
      else :
          wtime.append(int(Process[i][2])+wtime[-1])
          twt.append(wtime[-1])
      Process[i][2] = Process[i][2] - qt
      if (Process[i][2] > 0):  
        newprocess.append(Process[i])
    
    Process = newprocess
  for i in range(len(twt)):
    total_wtime = total_wtime + twt[i] - cpProcess[i]
    
  print('Total waiting time: ',total_wtime)
  print('Average waiting time: ',(total_wtime/n))