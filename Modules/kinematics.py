def avgspeed():
    d=float(input('Enter distance (m):'))
    t=float(input('Enter time (s):'))
    return round(d/t,2)
def displacement_nth():
    a=float(input('Enter acceleration (m/s^2):'))
    u=float(input('Enter initial velocity (m/s):'))
    n=int(input('Enter the nth second:'))
    return round(u+(a/2)*(2*n-1),2)
def maxheight():
    u=float(input('Enter initial velocity with which the object is thrown vertically (m/s):'))
    g= 9.81
    return round((u**2)/(2*g),2)
def timeofflight():
    u = float(input('Enter initial velocity with which the object is thrown vertically (m/s):'))
    g= 9.81
    return round((2*u)/g,2)
def projrange():
    u= float(input('Enter initial velocity with which the object is thrown  (m/s):'))
    k = float(input('Enter the angle which the initial velocity vector makes with the horizontal(degree):'))
    import math as w
    t=w.radians(k)
    s=(u**2)*w.sin(2*t)/9.81
    return round(s,2)
def projheight():
    import math as w
    u = float(input('Enter initial velocity with which the object is thrown  (m/s):'))
    k = float(input('Enter the angle which the initial velocity vector makes with the horizontal(degree):'))
    t = w.radians(k)
    return round((u**2)*((w.sin(t))**2)/(2*9.81),2)
def projtime():
    import math as w
    u = float(input('Enter initial velocity with which the object is thrown  (m/s):'))
    k = float(input('Enter the angle which the initial velocity vector makes with the horizontal(degree):'))
    t = w.radians(k)
    return round(((2*u)*w.sin(t))/9.81,2)



