#Escribe un archivo validar_contraseña.py que pida al usuario una contraseña
# verifique que cumpla los siguientes criterios:
def validator_password(password):
    if len(password) < 8:
        return "La contraseña debe tener al menos 8 caracteres"
    elif password.isalpha():
        return "La contraseña debe contener al menos un número"
    elif password.isnumeric():
        return "La contraseña debe contener al menos una letra"
    else:
        return "La contraseña es válida"
    
