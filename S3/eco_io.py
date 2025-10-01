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

# Mostrar los resultados por pantalla
print("\n" + "="*40)
print(f"Resultados de los cálculos:")
print(f"- Suma: {suma}")
print(f"- Media: {media}")
print(f"- El mayor número es: {mayor}")
print("="*40 + "\n")