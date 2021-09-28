# p3p2 - calculating area/volume

length = 173068.36
radius = length / 2
pi = 3.1415927

# Area of a square
area_of_square = length ** 2
print(area_of_square)

# Volume of a cube
vol_of_cube = area_of_square * length
print(vol_of_cube)

# Area of a circle
area_of_circle = pi * radius ** 2
print(area_of_circle)

# Volume of a sphere
vol_of_sphere = area_of_circle * (4/3) * radius
print(vol_of_sphere)

# Volume of a cylinder
vol_of_cylinder = area_of_circle * length
print(vol_of_cylinder)
