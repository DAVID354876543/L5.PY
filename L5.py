temperature  = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    outfit = "jacket"
    print("It's a cold day today.")
    print("Wear a", outfit)

else:
    outfit = "t-shirt"
    print("It's a warm day today.")
    print("Wear a", outfit)

is_raining = input("Is it raining? (yes/no): ")

if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
    print("It's very windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    print("The wind speed is moderate today.")
    print("No need for a windbreaker over your", outfit)

has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes, "to keep your feet dry.")

print("")
print("Weather check complete.")

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature, "°C")
print("Otfit chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker needed:", wind_speed > 30)
print("Shoes chosen:", shoes if has_puddles == "yes" else "regular shoes")
