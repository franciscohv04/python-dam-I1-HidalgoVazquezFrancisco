# Solicitar datos al usuario y calcular la edad con clasificación por tramos

# Importar la biblioteca datetime para obtener el año actual
from datetime import datetime

# Obtener el año actual
current_year = datetime.now().year

# Solicitar el nombre del usuario
nombre = input("Por favor, introduce tu nombre: ")

# Manejo de errores para la entrada del año de nacimiento
try:
    # Solicitar el año de nacimiento y convertirlo a entero
    ano_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))
    
    # Verificar que el año de nacimiento sea válido
    if ano_nacimiento > current_year or ano_nacimiento < (current_year - 120):
        print("Error: El año de nacimiento no es válido.")
    else:
        # Calcular la edad
        edad = current_year - ano_nacimiento
        
        # Clasificar por tramos de edad
        if edad < 18:
            tramo = "Menor de edad (menos de 18 años)"
        elif 18 <= edad <= 65:
            tramo = "Adulto (18 a 65 años)"
        else:
            tramo = "Adulto mayor (más de 65 años)"
        
        # Mostrar el resultado
        print(f"Hola {nombre}, tienes {edad} años y estás clasificado como: {tramo}")

# Manejar el error si el usuario no introduce un número válido.
except ValueError:
    print("Error: Por favor, introduce un número válido para el año de nacimiento.")