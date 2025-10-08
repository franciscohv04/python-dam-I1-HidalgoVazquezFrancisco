# Programa para calcular la media, suma y determinar el mayor de tres números

# Solicitar al usuario que ingrese tres números
num1 = float(input("Por favor, introduce el primer número: "))
num2 = float(input("Por favor, introduce el segundo número: "))
num3 = float(input("Por favor, introduce el tercer número: "))

# Calcular la suma de los tres números
suma = num1 + num2 + num3

# Calcular la media de los tres números
media = suma / 3

# Determinar cuál es el mayor de los tres números
mayor = max(num1, num2, num3)

# Función para comprobar si un número es primo
def es_primo(n):
    if n < 2:  # Los números menores que 2 no son primos
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Comprobar si cada número es primo
primo1 = es_primo(int(num1)) if num1.is_integer() else False
primo2 = es_primo(int(num2)) if num2.is_integer() else False
primo3 = es_primo(int(num3)) if num3.is_integer() else False

# Mostrar los resultados por pantalla
print("\n" + "="*40)
print(f"Resultados de los cálculos:")
print(f"- Suma: {suma}")
print(f"- Media: {media}")
print(f"- El mayor número es: {mayor}")
print(f"- ¿{num1} es primo? {'Sí' if primo1 else 'No'}")
print(f"- ¿{num2} es primo? {'Sí' if primo2 else 'No'}")
print(f"- ¿{num3} es primo? {'Sí' if primo3 else 'No'}")
print("="*40 + "\n")