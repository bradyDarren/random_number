#this program will simply convert the temperature from Fahrenheit to Celsius.

def convert_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * 9/5


def convert_to_fahrenheit(celsius_temp):
    return (celsius_temp * (9/5)) + 32


while True:
    user_input = input("Please select a temperature measurement type you would like"
                       " to CONVERT (C for Celsius/F for Fahrenheit): ").lower()
    try:
        if user_input == "f":
            user_input = input("Please enter a temp in degrees Fahrenheit: ")
            print("Your input was", float(user_input), "in F converts to", convert_to_celsius(float(user_input)), "in C.")
            break

        elif user_input == "c":
            user_input = input("Please enter a temp in degrees Celsius: ")
            print("Your input was", float(user_input), "in C converts to", convert_to_fahrenheit(float(user_input)), "in F.")
            break

        else:
            print("Please input a valid option")

    except ValueError:
        print("Please input a adequate numerical value next time.")
        break

