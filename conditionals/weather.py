temp = 75
forcast = "sunny"

if temp > 90:
    print("It's hot!\nStay inside!")
elif temp < 80 and forcast != "rainy":
    print("It's very warm!")
elif temp < 80 or forcast == "rainy":
    print("It's cool and rainy!")
elif temp == 75 and not forcast == "snow":
    print("It's 75 degrees!")
else:
    print("Enjoy the outdoor!")
print("Have a good day!")

raining = True
if raining:
    print("Bring an umbrella!")

if not raining:
    print("Leave the umbrella at home!")
else:
    print("Bring an umbrella!")