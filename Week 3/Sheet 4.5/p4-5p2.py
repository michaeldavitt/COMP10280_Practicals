# p4-5p2 - Area/volume Calculator

import math

length = float(input("Please enter a length: "))
pi = math.pi

if length >= 0:

    # Area of a square
    area_of_square = length ** 2
    print("The area of a square with side =", length, ":", area_of_square)

    # Volume of a cube
    vol_of_cube = area_of_square * length
    print("The volume of a cube with side =",  length, ":", vol_of_cube)

    # Area of a circle
    area_of_circle = pi * length ** 2
    print("The area of a circle with circle radius =", length, ":", area_of_circle)

    # Volume of a sphere
    vol_of_sphere = area_of_circle * (4 / 3) * length
    print("The volume of a sphere with circle radius =", length, ":", vol_of_sphere)

    # Volume of a cylinder
    vol_of_cylinder = area_of_circle * length
    print("The volume of a cylinder with circle radius = length and side =", length, ":", vol_of_cylinder)

else:
    print("Length must be >= 0. Please try again.")

print("Finished")
