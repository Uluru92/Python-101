# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

radius = 3.14
height = 5
circunference = 2*3.1415*radius
area_circulo = 3.1415*radius*radius
area_rectangulo = height*circunference
volumen = area_circulo*height
area_surface = area_circulo+area_circulo+area_rectangulo

print("The volumen is: ",volumen, "\nthe surface area is: ", area_surface)