# 📌 Verificador de números primos con manejo de errores

print("="*50)
print("🔢  VERIFICADOR DE NÚMEROS PRIMOS")
print("="*50)

try:
    # Pedir al usuario un número entero
    num_input = input("Introduce un número entero: ").strip()
    num = int(num_input)  # Convierte a entero

    # Verificar si el número es menor que 2
    if num < 2:
        print(f"⚠️  {num} no es un número primo.")
    else:
        # Comprobar si el número es primo
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(f"✅ {num} es un número primo.")
        else:
            print(f"❌ {num} no es un número primo.")

except ValueError:
    print("⚠️  Error: debes introducir un número entero válido.")
except Exception as e:
    print("⚠️  Error inesperado:", e)
