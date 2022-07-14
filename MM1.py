import random
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
def sim(Lambda,mu, n = 5000):    
    waiting_time, in_system_time, start_time, arrival_time, depart_time = Time(Lambda, mu, n)
    waiting_time_mean =stat.mean(waiting_time)
    in_system_time_mean = stat.mean(in_system_time) 
    return waiting_time_mean,in_system_time_mean

#Exponential Interarrival Time Distribution
def EITD(Lambda,n):
    t = []  
    for i in range(n):
        t.append(random.expovariate(Lambda)) #интервалы времени появления заявки
    return t

#Exponential Service Time Distribution 
def ESTD(mu,n):
    t = []    
    for i in range(n):
        t.append(random.expovariate(mu))  #интервалы времени обслуживания заявки
    return t

def Time(Lambda,mu,n):
    start_time,arrival_time, depart_time, in_system_time,wt = [],[],[],[],[]
    t = EITD(Lambda,n)  
    arrival_time = np.cumsum(t) #время прибытия события в заявки
    start_time.append(arrival_time[0]) #время начала обработки заявки
    estd = ESTD(mu,n) 
    depart_time.append(start_time[0] + estd[0]) # время, в которое закончилась обработка заявки
    for i in range(1,n):
        start_time.append(max(arrival_time[i],depart_time[i-1])) 
        depart_time.append(start_time[i]+estd[i])
        in_system_time.append(depart_time[i] - arrival_time[i]) #время события в системе
        wt.append(start_time[i] - arrival_time[i]) #время ожидания
    return wt,in_system_time, start_time,arrival_time, depart_time

def queue(n,start_time,arrival_time,depart_time): 
   start_id = 0
   dep_id = 0
   arrive_id = 0
   in_system = 0
   in_queue = 0
   full_in_system = 0
   full_queue = 0
   while dep_id < n:
       start = start_time[start_id] if start_id < n else float('inf')
       arrival = arrival_time if arrive_id < n else float("inf")
       departure = depart_time[dep_id]
       
       if start <= arrival and start <=departure:
           in_queue = -1
           start_id = start_id + 1
       elif arrival <= start and arrival <=departure:
           in_system = 1
           in_queue = 1
       else:
           in_system = -1
           dep_id = dep_id + 1
       full_in_system = full_in_system + in_system #количество заявок в системе
       full_queue = full_queue +in_queue #количество заявок в очереди
       
I,wt_average,in_system_average  = [],[],[]
Lambda = []
mu = []
# i = 1
# while i:
#     i = float(input("Lambda = "))
#     j = float(input("mu = "))
#     if(i!=0 or j!=0):
#         Lambda.append(i)
#         mu.append(j)
#     else:
#         break

# k =0 
# h = 0
# for i in mu:
#     k = k+1
#     for j in Lambda:
#         h= h+1
#         if h == len(mu)+1:
#             h = 0
#         if k == h:
#             print(sim(i, j))
#             I.append(i/j)
#             waiting_time_mean,in_system_time_mean, ful_time_mean = sim(i,j)
#             wt_average.append(waiting_time_mean)
#             in_system_average.append(in_system_time_mean)
            

z =0.2 
while z < 0.3:
    z = z+0.001
    mu.append(z)
for i in range(len(mu)):
    Lambda.append(0.2)
k =0 
h = 0
for i in mu:
    k = k+1
    for j in Lambda:
        h= h+1
        if h == len(mu)+1:
            h = 0
        if k == h:
            print(sim(i, j))
            I.append(i/j)
            waiting_time_mean,in_system_time_mean = sim(i,j)
            wt_average.append(waiting_time_mean)
            in_system_average.append(in_system_time_mean)
            
plt.figure()
plt.plot(I,in_system_average)
plt.figure()
plt.hist(in_system_average,100)
