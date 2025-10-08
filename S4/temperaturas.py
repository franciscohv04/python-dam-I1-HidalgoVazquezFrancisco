# 🌡️ Conversor de Temperaturas Completo
# Permite convertir entre Celsius, Fahrenheit y Kelvin

print("="*50)
print("🌡️  CONVERSOR DE TEMPERATURAS UNIVERSAL")
print("="*50)

# Mostrar opciones de unidades
print("Unidades disponibles:")
print("1️⃣  Celsius (°C)")
print("2️⃣  Fahrenheit (°F)")
print("3️⃣  Kelvin (K)")

# Pedir unidad de origen
origen = input("\nIntroduce el número de la unidad de ORIGEN: ")

# Pedir temperatura
temp = float(input("Introduce la temperatura que deseas convertir: "))

# Pedir unidad de destino
destino = input("Introduce el número de la unidad de DESTINO: ")

print("\n" + "-"*50)

# Convertir la temperatura según las opciones
resultado = None

# Primero, convertir todo a Celsius como base
if origen == "1":  # Celsius
    celsius = temp
elif origen == "2":  # Fahrenheit
    celsius = (temp - 32) * 5/9
elif origen == "3":  # Kelvin
    celsius = temp - 273.15
else:
    print("⚠️  Unidad de origen no válida.")
    exit()

# Luego, convertir desde Celsius a la unidad de destino
if destino == "1":  # Celsius
    resultado = celsius
    unidad = "°C"
elif destino == "2":  # Fahrenheit
    resultado = (celsius * 9/5) + 32
    unidad = "°F"
elif destino == "3":  # Kelvin
    resultado = celsius + 273.15
    unidad = "K"
else:
    print("⚠️  Unidad de destino no válida.")
    exit()

# Mostrar el resultado
print(f"✅ {temp:.2f} en la unidad elegida equivale a {resultado:.2f} {unidad}")
print("-"*50)
print("Conversión completada con éxito.")
print("="*50)
