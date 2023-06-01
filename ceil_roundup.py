import math


def paint_wall(height, width, area_covered="7"):
    number_of_cans_needed = (width * height) / int(area_covered)
    #print(number_of_cans_needed)
    cans_needed = math.ceil(number_of_cans_needed)
    #print(cans_needed)
    print(f"You will need {cans_needed} cans of paint")


#paint_wall(14, 38)

height = int(input("Enter the height of wall in meters: "))
width = int(input("Enter the width of wall in meters: "))
#area_coverage = int(input("Enter the area to be covered in sq.meters: "))

paint_wall(height, width)