# Define variables for emissions data
transportation_emissions = 1000 # lbs CO2 per flight
food_emissions = 500 # lbs CO2 per year
energy_emissions = 1000 # lbs CO2 per year
waste_emissions = 100 # lbs CO2 per year

# Ask the user for input
num_flights = int(input("How many flights do you take per year?"))
daily_energy_usage = float(input("How many kilowatt-hours of energy do you use per day?"))
waste_generated = float(input("How many pounds of waste do you generate per year?"))

# Calculate the user's carbon footprint
carbon_footprint = (num_flights * transportation_emissions + food_emissions + daily_energy_usage * energy_emissions + waste_generated * waste_emissions) / 2000

# Output the result
print("Your carbon footprint is approximately", carbon_footprint, "metric tons of CO2 per year.")
print("Consider reducing your transportation emissions by taking public transportation, or eating a more plant-based diet to reduce your food emissions.")
