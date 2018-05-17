"""In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
(MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPGto L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units."""

def fuel_efficiency():
    american_reading = float(input("Fuel efficiency in MPG: "))
    #1mpg=235.215/100km
    canadian_reading = american_reading*(235.215)
    print("That willbe %.3f/100km canadian fuel efficiency"%canadian_reading)

fuel_efficiency()
