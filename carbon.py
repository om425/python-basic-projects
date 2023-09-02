e=float(0.85)
p=float(2.653)
w=int(100)
l=float(2.983)
electricit= float(input("How many kilowatt-hours of energy do you use per month?:  "))
petrol= float(input("how many litre of petrol do you use per month?:  "))

lpg= float(input("how many LPG gas cylinder do you use per month?:  "))

carbon_footprint = int((electricit * e + petrol *p +lpg*l))
# Output the result
print("Your carbon footprint is approximately", carbon_footprint,"kg of CO2 per month.")
if(carbon_footprint<=100):
    print("You have silver footprints")
else:
    print("You have black footprints")
print("Consider reducing your transportation emissions by taking public transportation, or eating a more plant-based diet to reduce your food emissions.")






