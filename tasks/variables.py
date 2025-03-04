first_name  = "Valentyn"
last_name = "Medvediuk"
full_name = first_name + " " + last_name
country = "Ukraine"
city = "Lviv"
age = 23
year = 2025
is_merried = False
is_true = True
is_light = is_true

# Declare multiple variable on one line
personal_data = "Name: {full_name}; Country: {country}; City: {city}; Age: {age}; Married: {is_merried}; Light: {is_light}"
print(f"Personal data: " + personal_data.format(full_name=full_name, country=country, city=city, age=age, is_merried=is_merried, is_light=is_light))

#Check the data type of all your variables using type() built-in function
all_pesonal_data_types = {
    "first_name": type(first_name), 
    "last_name": type(last_name), 
    "country": type(country), 
    "city": type(city),
    "age": type(age), 
    "is_merried": type(is_merried), 
    "is_light": type(is_light)
    }

for key, value in all_pesonal_data_types.items():
    print(f"name: {key}; type: {value}")


# Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
print(len(first_name) + len(last_name))

#Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4
total = num_one + num_two

#Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

#Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_one % num_two

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

radius = int(input("Enter the radius of the circle: "))
area_of_circle = 3.14 *radius ** 2 #area_of_circle = 3.14 *radius ** 2
circum_of_circle = 2 * 3.14 * radius
print(f"Area of circle: {area_of_circle}; Circumference of circle: {circum_of_circle}")


#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
country = input("Enter your country: ") 
age = input("Enter your age: ")

print(f"Personal data: " + full_name + ", " + country + ", " + age)