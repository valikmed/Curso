import requests
import csv
import pandas as pd
import numpy as np
from tasks.validar_contraseña import validator_password

google = requests.get("https://google.com")
print(google.status_code)

with open("prueba.csv") as csv_file:
    lector = csv.reader(open("prueba.csv"))
    for row in lector:
        print(row)

print(validator_password(input("Enter your password: ")))