def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length: The length of the rectangle
    width: The width of the rectangle
    
    Returns:
    The area of the rectangle (length * width)
    """
    area = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
result = calculate_area(length, width)
print(f"The area of the rectangle is: {result}")
#Cris Jay Hubilla