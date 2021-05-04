
def timer(t):
    import time
    while t:
        x,y = divmod(t,3600)
        y,z = divmod(y,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(x,y,z)
        print(timer,end="\r" )
        time.sleep(1)
        t -= 1

    print('TIME UP!')

