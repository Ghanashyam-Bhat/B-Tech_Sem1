def Circle():
    import math
    r=float(input("Enter the radius of the circle: "))
    area_circle=math.pi*r*r
    print (area_circle)


def Triangle():
    x1=float(input("Enter x coordinate of point A: "))
    x2=float(input("Enter x coordinate of point B: "))
    x3=float(input("Enter x coordinate of point C: "))
    y1=float(input("Enter y coordinate of point A: "))
    y2=float(input("Enter y coordinate of point B: "))
    y3=float(input("Enter y coordinate of point C: "))
    area_triangle=abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))/2
    print("Area of Triangle= ",area_triangle)

def Square():
    x=input("Do you want to give coordinates of the corners or diagonals? Press C for corners and D for diagonals: ")
    if x=='C' or x=='c':
      x1=float(input("Enter x coordiante of point A: "))
      x2=float(input("Enter x coordinate of point B: "))
      x3=float(input("Enter x coordinate of point C: "))
      x4=float(input("Enter x coordinate of point D: "))
      y1=float(input("Enter y coordinate of point A: "))
      y2=float(input("Enter y coordinate of point B: "))
      y3=float(input("Enter y coordinate of point C: "))
      y4=float(input("Enter y coordinate of point D: "))
      area_square=(((x2-x1)**2+(y2-y1)**2)**(1/2))**2
      print("Area of square: ",area_square)
    elif x=='D' or x=='d':
      x_1=float(input("Enter the x cordinate of the 1st point: "))
      x_2=float(input("Enter the x cordinate of the 2nd point: "))
      y_1=float(input("Enter the y cordinate of the 1st point: "))
      y_2=float(input("Enter the x cordinate of the 2nd point: "))
      area_square1=((((x_2-x_1)**2+(y_2-y_1)**2)**0.5)**2)/2
      print("Area of square is: ",area_square1)

def Rectangle():
      x1=float(input("Enter x coordiante of point A: "))
      x2=float(input("Enter x coordinate of point B: "))
      x3=float(input("Enter x coordinate of point C: "))
      x4=float(input("Enter x coordinate of point D: "))
      y1=float(input("Enter y coordinate of point A: "))
      y2=float(input("Enter y coordinate of point B: "))
      y3=float(input("Enter y coordinate of point C: "))
      y4=float(input("Enter y coordinate of point D: "))
      b=((x2-x1)**2+(y2-y1)**2)**0.5
      h=((x3-x2)**2+(y3-y2)**2)**0.5
      area_rectangle=b*h
      print("Area of Rectangle is: ",area_rectangle)    

def Trapezium():
      x1=float(input("Enter x coordiante of point A: "))
      x2=float(input("Enter x coordinate of point B: "))
      x3=float(input("Enter x coordinate of point C: "))
      x4=float(input("Enter x coordinate of point D: "))
      y1=float(input("Enter y coordinate of point A: "))
      y2=float(input("Enter y coordinate of point B: "))
      y3=float(input("Enter y coordinate of point C: "))
      y4=float(input("Enter y coordinate of point D: "))
      a=((x2-x1)**2+(y2-y1)**2)**0.5
      b=((x4-x3)**2+(y4-y3)**2)**0.5
      c=((x3-x2)**2+(y3-y2)**2)**0.5
      d=((x4-x1)**2+(y4-y1)**2)**0.5
      area_trapezium=(1/2)*((d**2-(abs((a-b))**2)/4)**0.5)*(a+b)
      print("Area of trapezium: ",area_trapezium)

def Sphere():
    r=float(input("Enter the radius of sphere: "))
    area_sphere=4*3.14*r**2
    print("Area of sphere is: ",area_sphere)

def Cube():
    x1=float(input("Enter the x coordiante of any 1 point:"))
    y1=float(input("Enter the y coordiante of the same point: "))
    x2=float(input("Enter the x coordiante of another point:"))
    y2=float(input("Enter the y coordiante of the same point: "))
    area_cube=6*(((x2-x1)**2-(y2-y1)**2)**0.5)**2
    print("Area of cube: ",area_cube)

def Cone():
   import math
   r=float(input("Enter radius of the cone: "))
   h=float(input("Enter height of the cone: "))
   area_cone=math.pi*r*(r+(r**2+h**2)**0.5)
   print("Area of Cone is: ",area_cone)

def Cylinder():
   import math
   r=float(input("Enter radius of the cylinder: "))
   h=float(input("Enter height of the cylinder: "))
   area_cylinder=2*math.pi*r*h+2*3.14*r**2
   print("Area of cylinder is: ",area_cylinder)


def Pentagon():
    x1=float(input("Enter x coordinate of point A: "))
    x2=float(input("Enter x coordinate of point B: "))
    x3=float(input("Enter x coordinate of point C: "))
    x4=float(input("Enter x coordinate of point D: "))
    x5=float(input("Enter x coordinate of point E: "))
    y1=float(input("Enter y coordinate of point A: "))
    y2=float(input("Enter y coordinate of point B: "))
    y3=float(input("Enter y coordinate of point C: "))
    y4=float(input("Enter y coordinate of point D: "))
    y5=float(input("Enter y coordinate of point E: "))
    area1=abs((x1*(y2-y5)+x2*(y5-y1)+x5  *(y1-y2)))/2
    area2=abs((x2*(y3-y5)+x3*(y5-y2)+x5*(y2-y3)))/2
    area3=abs((x3*(y4-y5)+x4*(y5-y3)+x5*(y3-y4)))/2
    area_irrpent=area1+area2+area3
    print("Area of irregular pentagon: ",area_irrpent)


def Hexagon():
    x1=float(input("Enter x coordinate of point A: "))
    x2=float(input("Enter x coordinate of point B: "))
    x3=float(input("Enter x coordinate of point C: "))
    x4=float(input("Enter x coordinate of point D: "))
    x5=float(input("Enter x coordinate of point E: "))
    x6=float(input("Enter x coordinate of point F: "))
    y1=float(input("Enter y coordinate of point A: "))
    y2=float(input("Enter y coordinate of point B: "))
    y3=float(input("Enter y coordinate of point C: "))
    y4=float(input("Enter y coordinate of point D: "))
    y5=float(input("Enter y coordinate of point E: "))
    y6=float(input("Enter y coordinate of point F: "))
    a1=abs((x1*(y2-y6)+x2*(y6-y1)+x6*(y1-y2)))/2
    a2=abs((x2*(y3-y6)+x3*(y6-y2)+x6*(y2-y3)))/2
    a3=abs((x3*(y4-y6)+x4*(y6-y3)+x6*(y3-y4)))/2
    a4=abs((x4*(y5-y6)+x5*(y6-y4)+x6*(y4-y5)))/2
    area_irrhex=a1+a2+a3+a4
    print("Area of irregular Hexagon is: ",area_irrhex)

def Heptagon():
    x1=float(input("Enter x coordinate of point A: "))
    x2=float(input("Enter x coordinate of point B: "))
    x3=float(input("Enter x coordinate of point C: "))
    x4=float(input("Enter x coordinate of point D: "))
    x5=float(input("Enter x coordinate of point E: "))
    x6=float(input("Enter x coordinate of point F: "))
    x7=float(input("Enter x coordinate of point G: "))
    y1=float(input("Enter y coordinate of point A: "))
    y2=float(input("Enter y coordinate of point B: "))
    y3=float(input("Enter y coordinate of point C: "))
    y4=float(input("Enter y coordinate of point D: "))
    y5=float(input("Enter y coordinate of point E: "))
    y6=float(input("Enter y coordinate of point F: "))
    y7=float(input("Enter y coordinate of point G: "))
    a1=abs((x1*(y2-y7)+x2*(y7-y1)+x7*(y1-y2)))/2
    a2=abs((x2*(y3-y7)+x3*(y7-y2)+x7*(y2-y3)))/2
    a3=abs((x3*(y5-y7)+x5*(y7-y3)+x7*(y3-y5)))/2
    a4=abs((x3*(y4-y5)+x4*(y5-y3)+x5*(y3-y4)))/2
    a5=abs((x5*(y6-y7)+x6*(y7-y5)+x7*(y5-y6)))/2
    area_heptagon=a1+a2+a3+a4+a5
    print("Area of Heptagon is: ",area_heptagon)

def Kite():
    x1=float(input("Enter x coordiante of point A: "))
    x2=float(input("Enter x coordinate of point B: "))
    x3=float(input("Enter x coordinate of point C: "))
    x4=float(input("Enter x coordinate of point D: "))
    y1=float(input("Enter y coordinate of point A: "))
    y2=float(input("Enter y coordinate of point B: "))
    y3=float(input("Enter y coordinate of point C: "))
    y4=float(input("Enter y coordinate of point D: "))
    p=((x3-x1)**2+(y3-y1)**2)**0.5
    q=((x4-x2)**2+(y4-y2)**2)**0.5
    area_kite=(p*q)*(1/2)
    print("Area of Kite is: ",area_kite)

