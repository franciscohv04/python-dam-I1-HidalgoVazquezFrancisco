# Solicitar datos al usuario y calcular la edad con clasificación por tramos, incluyendo día y mes

# Importar la biblioteca datetime para obtener la fecha actual
from datetime import datetime

# Obtener la fecha actual
current_date = datetime.now()

# Solicitar el nombre del usuario
nombre = input("Por favor, introduce tu nombre: ")

# Manejo de errores para la entrada de la fecha de nacimiento
try:
    # Solicitar día, mes y año de nacimiento y convertirlos a enteros
    dia_nacimiento = int(input("Por favor, introduce tu día de nacimiento (1-31): "))
    mes_nacimiento = int(input("Por favor, introduce tu mes de nacimiento (1-12): "))
    ano_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))

    # Verificar que la fecha sea válida
    if (ano_nacimiento > current_date.year or ano_nacimiento < (current_date.year - 120) or
        mes_nacimiento < 1 or mes_nacimiento > 12 or
        dia_nacimiento < 1 or dia_nacimiento > 31):
        print("Error: La fecha de nacimiento no es válida.")
    else:
        # Crear fecha de nacimiento
        fecha_nacimiento = datetime(ano_nacimiento, mes_nacimiento, dia_nacimiento)
        
        # Calcular la edad exacta
        edad = current_date.year - fecha_nacimiento.year - ((current_date.month, current_date.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        
        # Determinar el signo del zodiaco
        if (mes_nacimiento == 3 and dia_nacimiento >= 21) or (mes_nacimiento == 4 and dia_nacimiento <= 19):
            signo = "Aries"
        elif (mes_nacimiento == 4 and dia_nacimiento >= 20) or (mes_nacimiento == 5 and dia_nacimiento <= 20):
            signo = "Tauro"
        elif (mes_nacimiento == 5 and dia_nacimiento >= 21) or (mes_nacimiento == 6 and dia_nacimiento <= 20):
            signo = "Géminis"
        elif (mes_nacimiento == 6 and dia_nacimiento >= 21) or (mes_nacimiento == 7 and dia_nacimiento <= 22):
            signo = "Cáncer"
        elif (mes_nacimiento == 7 and dia_nacimiento >= 23) or (mes_nacimiento == 8 and dia_nacimiento <= 22):
            signo = "Leo"
        elif (mes_nacimiento == 8 and dia_nacimiento >= 23) or (mes_nacimiento == 9 and dia_nacimiento <= 22):
            signo = "Virgo"
        elif (mes_nacimiento == 9 and dia_nacimiento >= 23) or (mes_nacimiento == 10 and dia_nacimiento <= 22):
            signo = "Libra"
        elif (mes_nacimiento == 10 and dia_nacimiento >= 23) or (mes_nacimiento == 11 and dia_nacimiento <= 21):
            signo = "Escorpio"
        elif (mes_nacimiento == 11 and dia_nacimiento >= 22) or (mes_nacimiento == 12 and dia_nacimiento <= 21):
            signo = "Sagitario"
        elif (mes_nacimiento == 12 and dia_nacimiento >= 22) or (mes_nacimiento == 1 and dia_nacimiento <= 19):
            signo = "Capricornio"
        elif (mes_nacimiento == 1 and dia_nacimiento >= 20) or (mes_nacimiento == 2 and dia_nacimiento <= 18):
            signo = "Acuario"
        else:
            signo = "Piscis"

        # Clasificar por tramos de edad
        if edad < 18:
            tramo = "Menor de edad (menos de 18 años)"
        elif 18 <= edad <= 65:
            tramo = "Adulto (18 a 65 años)"
        else:
            tramo = "Adulto mayor (más de 65 años)"
        
        # Mostrar el resultado con formato mejorado
        print("\n" + "="*40)
        print(f"¡Hola {nombre}! Aquí está tu información:")
        print(f"- Edad exacta: {edad} años")
        print(f"- Signo del zodiaco: {signo}")
        print(f"- Clasificación: {tramo}")
        print("="*40 + "\n")

# Manejar el error si el usuario no introduce un número válido
except ValueError:
    print("Error: Por favor, introduce números válidos para la fecha de nacimiento.")
except ValueError:
    print("Error: La fecha ingresada no es válida.")