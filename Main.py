import Create 
import Function


Process = []
n ,r1, r2, r3 = 20,40,40,20
Process = Create.create(n, r1, r2, r3)
print('ProcessName\tArrivalTime\tBurstTime')
for i in range(len(Process)):
  print(Process[i][0],'\t\t',Process[i][1],'\t\t',Process[i][2])
print(' ')

Function.FCFS(Process, n)
print('---------------------------')
Function.SJF(Process, n)
print('---------------------------')
Function.RR(Process, n, 4)
print('---------------------------')