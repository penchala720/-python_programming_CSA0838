#AREA OF THE CIRCLE

radius = float(input("enter the radius of circle :"))
area = float(3.14*radius*radius)  #casting into float is Optional --->3.14 already a float value
print("Area of circle is without format : ",area)
print("Area of circle is with format : ",format(area,'.4f'))
