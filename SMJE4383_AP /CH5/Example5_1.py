#Conversion Program 

def celcius_to_fahrenheit(celsius_float) :
   #""""""Convert Celcius to Farenheit""""""
    return celsius_float*1.8 +32
#    #main part of the program 
print("convert Celcius to Farenheit")
celsius_float= float(input("Enter a Celcius temp:"))

#call the conversion function 
fahrenheit_float = celcius_to_fahrenheit(celsius_float)
#print the returned value 
print(celsius_float, "converts to", fahrenheit_float, "Farenheit")