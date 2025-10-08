# Conversor de Temperaturas
# De grados Celsius a Kelvin o Fahrenheit

print("="*45)
print("🌡️  CONVERSOR DE TEMPERATURAS")
print("="*45)

# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Mostrar opciones de conversión
print("\n¿A qué unidad deseas convertir?")
print("1️⃣  Kelvin (K)")
print("2️⃣  Fahrenheit (°F)")

# Pedir elección
opcion = input("Elige una opción (1 o 2): ")

print("\n" + "-"*45)

# Calcular según la opción elegida
if opcion == "1":
    kelvin = celsius + 273.15
    print(f"✅ {celsius:.2f} °C equivalen a {kelvin:.2f} K")
elif opcion == "2":
    fahrenheit = (celsius * 9/5) + 32
    print(f"✅ {celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
else:
    print("⚠️  Opción no válida. Por favor, elige 1 o 2.")

print("-"*45)
print("Conversión completada con éxito.")
print("="*45)
