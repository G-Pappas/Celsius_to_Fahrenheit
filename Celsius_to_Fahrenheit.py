"""
This application convert Celcius degrees to Fahrenheit degrees
"""
#function to check if user input is a valid temperature and convertion to Fahrenheit
def CtoF(celcius):
    if float(celcius) > -273.15:
        Fahrenheit = float(celcius)*9/5+32
        return Fahrenheit
    else:
        return ("Can't get under -273.15 Celcius")


celcius = input("Give me Celcius degrees: ")
print (celcius, "Celcius degrees are ", CtoF(celcius),  " Fahrenheit degrees")


input("Press enter to exit ")
