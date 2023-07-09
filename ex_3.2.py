import math

def is_triangle(a, b, c):
    # Check if the given sides can form a triangle
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

def calculate_triangle_properties(a, b, c):
    if is_triangle(a, b, c):
        # Calculate the perimeter of the triangle
        perimeter = a + b + c
        
        # Calculate the semi-perimeter
        s = perimeter / 2
        
        # Calculate the surface area using Heron's formula
        surface_area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return perimeter, surface_area
    else:
        return None

# Example usage
a = 3
b = 4
c = 5

triangle_properties = calculate_triangle_properties(a, b, c)
if triangle_properties:
    perimeter, surface_area = triangle_properties
    print("Perimeter:", perimeter)
    print("Surface Area:", surface_area)
else:
    print("These side lengths cannot form a triangle.")
