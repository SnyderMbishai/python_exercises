"""Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with."""

def room_area():
    width = float(input("What's the room's width in metres? "))
    length = float(input("What's its length? "))
    area = width*length
    print ("The room's area is %s square metres" % area)

room_area()
