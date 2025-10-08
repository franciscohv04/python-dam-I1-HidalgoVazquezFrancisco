# 🌡️ Conversor de Temperaturas Universal con manejo de errores simplificado

print("="*50)
print("🌡️  CONVERSOR DE TEMPERATURAS UNIVERSAL")
print("="*50)

print("Unidades disponibles:")
print("1️⃣  Celsius (°C)")
print("2️⃣  Fahrenheit (°F)")
print("3️⃣  Kelvin (K)")

try:
    # Pedir unidad de origen
    origen = input("\nIntroduce el número de la unidad de ORIGEN: ").strip()
    if origen not in ("1", "2", "3"):
        print("⚠️  Unidad de origen no válida. Por favor selecciona 1, 2 o 3.")
        exit()

    # Pedir temperatura
    temp = float(input("Introduce la temperatura que deseas convertir: "))

    # Pedir unidad de destino
    destino = input("Introduce el número de la unidad de DESTINO: ").strip()
    if destino not in ("1", "2", "3"):
        print("⚠️  Unidad de destino no válida. Por favor selecciona 1, 2 o 3.")
        exit()

    print("\n" + "-"*50)

    # Convertir a Celsius como base
    if origen == "1":  # Celsius
        celsius = temp
    elif origen == "2":  # Fahrenheit
        celsius = (temp - 32) * 5/9
    elif origen == "3":  # Kelvin
        celsius = temp - 273.15

    # Convertir desde Celsius a destino
    if destino == "1":  # Celsius
        resultado = celsius
        unidad = "°C"
    elif destino == "2":  # Fahrenheit
        resultado = (celsius * 9/5) + 32
        unidad = "°F"
    elif destino == "3":  # Kelvin
        resultado = celsius + 273.15
        unidad = "K"

    # Mostrar el resultado
    print(f"✅ {temp:.2f} en la unidad elegida equivale a {resultado:.2f} {unidad}")
    print("-"*50)
    print("Conversión completada con éxito.")
    print("="*50)

except ValueError:
    print("\n⚠️  Error: asegúrate de introducir un número válido para la temperatura.")
except Exception as e:
    print("\n⚠️  Error inesperado:", e)
