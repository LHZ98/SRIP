import numpy as np
import cvxpy as cp
import random
import math
#parameters
acel_max = 5
dcel_max = -5
Vmax = 30
s_st = 2
s_go = 18
car_list = []
NumStep = 5
for i in range(5):
    car_list.append(i * 10 + int(np.random.rand() * 10))


def cal_v(prev, ego):
    if (prev - ego) < 0:
        return Vmax / 2 * (1- math.cos((50 - (ego - prev) - s_st) / (s_go - s_st) * math.pi))
    if (prev - ego) <= s_st:
        return 0
    elif (prev - ego) < s_go:
        return Vmax / 2 * (1- math.cos((prev - ego - s_st) / (s_go - s_st) * math.pi))
    else:
        return Vmax

print(car_list)
for j in range(NumStep):
    speed = []
    result = car_list.copy()
    for i in range(len(car_list)):
        if i == len(car_list) - 1:
            result[-1] += 0.01 * cal_v(car_list[0], car_list[i])
            speed.append(cal_v(50 + car_list[0], car_list[i]))
        else:
            result[i] += 0.01 * cal_v(car_list[i + 1], car_list[i])
            speed.append(cal_v(car_list[i + 1], car_list[i]))
    cav_a = 0.1 * (car_list[-1] - car_list[3] - 10) +  (-0.05) * (speed[3] - 15) + \
    (-0.2) * (car_list[3] - car_list [2] -10) + (0.01) * (speed[2] - 15)
    result[-1] += cav_a*0.01
    print(cav_a)
    car_list = result.copy()
    distance = result[0]
    for i in range(len(result)):
        result[i] -= distance
    print(result)

x = cp.Variable(n)


    
    

        
    
    
