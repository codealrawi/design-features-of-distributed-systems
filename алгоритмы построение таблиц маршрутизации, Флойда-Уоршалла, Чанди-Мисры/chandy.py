print(
'''

            A     B     C
            0    0        0
P0      -   0     0     0
        ----------------
            0    0        0
        +   0     1     0
-------------------------------
          0     1     0
P1    -  0    1     0
      ------------------
      +   0     0     0
          2     0     0
-------------------------------
P3      -   2    0     0
            0     0     0
        ----------------------
        +  2    0     0
            3     1     3
--------------------------------
            5     1     3


A = 5 INSTANCES (пример)
B = 1 INSTANCES (пример)
C = 3 INSTANCES (пример)
'''
)

from operator import add

def detect(process, allocation, request, work):
   n=len(process)
   finish=[False]*n

   for i in range(n):
      if allocation[i]==[0]*3:
         finish[i]=True

   for i in range(n):
      if finish[i]==False and request[i]<=work:
         work=list(map(add, work, allocation[i]))
         finish[i]=True

   print(finish)
   for i in range(n):
      if finish[i]==False:
         print('Deadlock occurs for the process {}'.format(i))
      if finish==[True]*n:
         print('No Deadlock!')

if __name__=='__main__':
   process=[0, 1, 2]

   allocation=   [[0, 1, 0],
               [2, 0, 0],
               [3, 0, 3]]

   request=    [[0, 0, 0],
            [0, 1, 0],   # [2, 1, 2]  DEADLOCK WILL HAPPEND IN PROCESS NO!
            [0, 0, 0]]

   available=[0, 0, 0]

   detect(process, allocation, request, available)
