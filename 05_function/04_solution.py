import math

def circle_stats(radius):
    area=radius*radius*math.pi
    circumference=2*math.pi*radius
    return area,circumference
    
a,c=circle_stats(3)
print("Area",a,"Circumference",c)