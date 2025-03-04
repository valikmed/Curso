#°F = (°C × 9/5) + 32
#C = (°F - 32) × 5/9
tempreture_in_celcius = float(input("Enter temperature in Celcius: "))
tempreture_in_fahrenheit = (tempreture_in_celcius * 9/5) + 32
print(f"{tempreture_in_celcius} Celcius is equal to {tempreture_in_fahrenheit} Fahrenheit")

temperature_in_farnheit = float(input("Enter temperature in Farenheit: "))
temperature_in_celcius = (temperature_in_farnheit -32)*5/9
print(f"{temperature_in_farnheit} Farhrenheit is equal to {temperature_in_celcius} Celcius")