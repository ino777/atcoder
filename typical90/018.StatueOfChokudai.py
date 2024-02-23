T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

import math

omega = 2*math.pi/T
def y(t):
    return (-L/2)*math.sin(omega*t)

def z(t):
    return L/2*(1-math.cos(omega*t))


for _ in range(Q):
    et = int(input())
    theta = math.atan(z(et)/math.sqrt(X**2+(Y-y(et))**2)) * 180/math.pi
    print(theta)