# first_name, last_name, age, city, country = '', '', '', '', ''
# print(input("First Name: "), input("Last Name: "), input("Age: "), input("City: "), input("Country: "), sep=', ')

# first_name_your_friend, last_name_your_friend, age_your_friend, city_your_friend, country_your_friend = "Valentyn", "Medvediuk", 23, "Lviv", "Ukraine"
# print(first_name_your_friend, last_name_your_friend, age_your_friend, city_your_friend, country_your_friend, sep=', ')

# age_your_friend += 1
# print(age_your_friend)
# age_your_friend -= 1
# print(age_your_friend)
# age_your_friend *= 2
# print(age_your_friend)
# age_your_friend /= 2
# print(age_your_friend)
# age_your_friend %= 2
# print(age_your_friend)

# num_int = 10
# print(type(num_int), num_int)

# num_int_to_float = float(num_int)
# print(type(num_int_to_float), num_int_to_float)

# num_int_to_str = str(num_int)
# print(type(num_int_to_str), num_int_to_str)

# none_num_value = None
# none_num_value_to_bool = bool(none_num_value)
# print(type(none_num_value_to_bool), none_num_value_to_bool) # When we convert None to boolean, it returns False while other values return True


# fun_abs = abs(-10.99866)
# print(fun_abs)

# fun_pow = pow(2, 3)
# print(fun_pow)

# If value is not an integer, it will round to the nearest integer
# fun_round = round(2.6789) 
# print(fun_round)

# fun_max = max(1, 2, 3, 4, 5)
# print(fun_max)

# fun_min = min(1, 2, 3, 4, 5)
# print(fun_min)

# # This function returns the sum of the list
# fun_mean = sum([1, 2, 3, 4, 5]) / len([1, 2, 3, 4, 5])
# print(fun_mean) 

# # This function returns true if all values are not None
# func_all_return_true = all([1, 2, 3, 4, 3])
# print(func_all_return_true)
# func_all_return_false = all([1, None, 3, 4, 3])
# print(func_all_return_false)

# This function returns true if any value is not None
# any_value = any([1, None, 3, 4, 3])
# print(any_value)
# any_value = any([None, None, None, None, None])
# print(any_value)


# # This function returns the ASCII value of the character
# ascii_value = ord('a'.upper())
# print(ascii_value)

# # This function retuns the value of a binary number
# bin_value = bin(10)
# print(bin_value)

# # This function returns the value of a hexadecimal number
# hex_value = hex(10)
# print(hex_value)
 
 
 
# is_true = True
# check_is_true = bool(is_true)
# print(check_is_true)

# # This function returns the value of a octal number
# oct_value = oct(10)
# print(oct_value)

# str_breakpoint = breakpoint(oct_value)
# print(str_breakpoint)


# byte_val = bytearray(10)
# print(byte_val)

# def calculate_sum(a, b):
#     result = a + b
#     # breakpoint() # Use it only for debugging
#     return result

# print(calculate_sum(5, 3))

# It part of code with calleble() return True if the oject and False if is value or other
def return_sum(a, b):
    return a + b

# print(return_sum(5, 3))

# callable_value = callable(return_sum)
# print(callable_value)

# value_chr = chr(100)
# print(value_chr)

classmethod_value = classmethod(return_sum)