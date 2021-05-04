def quadrilateral():
    print('For the Quadilateral ABCD:')
    XA = int(input('Enter the x coordinate of point A:'))
    YA = int(input('Enter the y coordinate of point A:'))
    XB = int(input('Enter the X coordinate of point B:'))
    YB = int(input('Enter the y coordinate of point B:'))
    XC = int(input('Enter the X coordinate of point C:'))
    YC = int(input('Enter the y coordinate of point C:'))
    XD = int(input('Enter the X coordinate of point D:'))
    YD = int(input('Enter the y coordinate of point D:'))
    if (XA-XB)==0:
        m1='z'
    else:
        m1 = (YA-YB)/(XA-XB)
    if (XB-XC)==0:
        m2='z'
    else:
        m2=(YB-YC)/(XB-XC)
    if (XC-XD)==0:
        m3='z'
    else:
        m3=(YC-YD)/(XC-XD)
    if (XA-XD)==0:
        m4='z'
    else:
        m4 = (YA-YD)/(XA - XD)

    def f(p,q,r,s):
         ((p-r)**2+(q-s)**2)**(1/2)
    AB=((XA-XB)**2+(YA-YB)**2)**(1/2)
    BC=((XB-XC)**2+(YB-YC)**2)**(1/2)
    CD=((XC-XD)**2+(YC-YD)**2)**(1/2)
    DA=((XD-XA)**2+(YD-YA)**2)**(1/2)
    AC=((XA-XC)**2+(YA-YC)**2)**(1/2)
    BD=((XB-XD)**2+(YB-YD)**2)**(1/2)
    if AB==BC and BC==CD and CD==DA:
        if AC==BD:
            print('Square')
        else:
            print('Rhombus')
    elif AB==CD and DA==BC and DA!=AB:
        if AC==BD:
            print('Rectangle')
        else:
            print('Parallelogram')
    elif m1==m3 and m2!=m4:

        print('Trapezium')
    elif m1!=m3 and m2==m4:
        print('Trapezium')
    elif AB==BC and CD==DA and AB!=CD:
        print('Kite')
    elif AB==DA and BC==CD and AB!=BC:
        print('Kite')
    else:
        print('Not a Special Quadrilateral')


