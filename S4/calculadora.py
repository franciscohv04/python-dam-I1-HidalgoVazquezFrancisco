import math

print("="*50)
print("🧮  CALCULADORA INTERACTIVA CON OPERADORES EXTENDIDOS")
print("="*50)

while True:
    print("\nSeleccione una operación:")
    print("1️⃣  Suma (+)")
    print("2️⃣  Resta (-)")
    print("3️⃣  Multiplicación (*)")
    print("4️⃣  División (/)")
    print("5️⃣  Potencia (**)")
    print("6️⃣  Módulo (%)")
    print("7️⃣  División entera (//)")
    print("8️⃣  Raíz cuadrada (sqrt)")
    print("0️⃣  Salir")

    opcion = input("Introduce el número de la operación: ").strip()

    if opcion == "0":
        print("👋 Gracias por usar la calculadora. ¡Adiós!")
        break

    try:
        if opcion == "8":  # Raíz cuadrada
            num = float(input("Introduce el número: "))
            if num < 0:
                print("⚠️  No se puede calcular la raíz de un número negativo.")
                continue
            resultado = math.sqrt(num)
            print(f"✅ La raíz cuadrada de {num} es {resultado:.2f}")
        else:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == "1":
                resultado = num1 + num2
                print(f"✅ {num1} + {num2} = {resultado}")
            elif opcion == "2":
                resultado = num1 - num2
                print(f"✅ {num1} - {num2} = {resultado}")
            elif opcion == "3":
                resultado = num1 * num2
                print(f"✅ {num1} * {num2} = {resultado}")
            elif opcion == "4":
                if num2 == 0:
                    print("⚠️  Error: División entre cero no permitida.")
                    continue
                resultado = num1 / num2
                print(f"✅ {num1} / {num2} = {resultado}")
            elif opcion == "5":
                resultado = num1 ** num2
                print(f"✅ {num1} ** {num2} = {resultado}")
            elif opcion == "6":
                if num2 == 0:
                    print("⚠️  Error: Módulo entre cero no permitido.")
                    continue
                resultado = num1 % num2
                print(f"✅ {num1} % {num2} = {resultado}")
            elif opcion == "7":
                if num2 == 0:
                    print("⚠️  Error: División entera entre cero no permitida.")
                    continue
                resultado = num1 // num2
                print(f"✅ {num1} // {num2} = {resultado}")
            else:
                print("⚠️  Opción no válida. Intenta de nuevo.")

    except ValueError:
        print("⚠️  Error: Debes ingresar números válidos.")
    except Exception as e:
        print(f"⚠️  Ocurrió un error inesperado: {e}")
