# 📌 Verificador de números primos paso a paso

print("="*60)
print("🔢  VERIFICADOR DE NÚMEROS PRIMOS PASO A PASO")
print("="*60)

try:
    # Pedir al usuario un número entero
    num_input = input("Introduce un número entero: ").strip()
    num = int(num_input)  # Convierte a entero

    # Verificar si el número es menor que 2
    if num < 2:
        print(f"⚠️  {num} no es un número primo.")
    else:
        es_primo = True
        print(f"\n🔹 Comprobando divisores de {num} desde 2 hasta {int(num**0.5)}...\n")
        
        # Comprobar si el número es primo paso a paso
        for i in range(2, int(num**0.5) + 1):
            print(f"Probando si {num} es divisible entre {i}...", end=" ")
            if num % i == 0:
                print(f"Sí, {i} es un divisor. → {num} NO es primo.")
                es_primo = False
                break
            else:
                print("No, sigue comprobando.")

        if es_primo:
            print(f"\n✅ {num} es un número primo.")

except ValueError:
    print("⚠️  Error: debes introducir un número entero válido.")
except Exception as e:
    print("⚠️  Error inesperado:", e)
