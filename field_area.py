"""Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres."""

def field_area():
    width = float(input("What's the field's width in feet? "))
    length = float(input("What's its length? "))
    area = width*length
    #43560 square feet makes an acre
    feet_to_acres = area / 43560
    print("The area of the field is %s acres" % feet_to_acres)

field_area()
