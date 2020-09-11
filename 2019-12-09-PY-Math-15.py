'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import math

c = int(input("Please enter the number of the corresponding question you want to see (26(CH:2 Q:6),5(CH:1 Q:5),16(CH:1 Q:6)\n")) 
 
if c == 26:    
    x = float(input("Please enter the mass \n"))
    y = float(input("Please enter the velocity/volume \n"))
    z = 1/2*x*(y**2)
    print("your KE = "+str(z)+"\n")
    
    z = x/y
    print("your density = "+str(z)+"\n")
    z = x*y
    print("your answer(multiplication) = "+str(z)+"\n")
    z = x**y
    print("your answer(exponents) = "+str(z))

elif c == 15:
    base = int(input("Enter with base length: "))# the randomly selected bases are: 5, 10, and 2
    height = int(input( "Enter with height: "))# the randomly selected heights are: 6, 4, and 5
    area = (base*height)/2
    print("The area is", area, "square units. \n")# the area measurements are: 15u^2, 20u^2, and 5u^2
    

    area = base*height
    print("The area(rectangle) is ", area, "square units. \n")
    area = base**3
    print("The volume (cube) is", area, "square units. \n")
    area = math.pi*height
    print("The area(Circumference) is", area, "square units. \n")

elif c == 16:
    radius = int(input("Enter with the length of the radius: ")) # the randomly selected Radii are: 4, 2, and 5
    h = 12
    area = math.pi*(radius**2)
    print("The area is", round(area, 2), "square units.") # The area measurements are: 50.24u^2, 12,56u^2, and 78.5u^2  
    
    area = 4/3*math.pi*(radius**3)
    print("The volume(Sphere) is", round(area, 2), "cubed units.")
    area = math.pi*(radius**2)
    print("The volume(Cylinder) is", round(area, 2), "cubed units.")
    area = math.pi*(radius**2)*h/3
    print("The volume(cone) is", round(area, 2), "cubed units.")
else:
    print("invalid input")

