# Programa que procesa una lista de números separados por comas

# Pedir al usuario la lista de números
entrada = input("Introduce una lista de números separados por comas: ")

# Convertir a lista de floats, eliminando espacios extra
numeros = [float(x.strip()) for x in entrada.split(",")]

# Calcular suma, media y máximo
suma = sum(numeros)
media = suma / len(numeros)
maximo = max(numeros)

# Detectar duplicados
duplicados = set([x for x in numeros if numeros.count(x) > 1])

# Calcular cuadrados
cuadrados = [x**2 for x in numeros]

# Mostrar resultados con formato vistoso
print("\n" + "="*50)
print("📊  RESULTADOS DEL ANÁLISIS DE NÚMEROS")
print("="*50)
print(f"🔢 Números introducidos: {numeros}")
print(f"🧮 Suma total: {suma:.2f}")
print(f"📈 Media: {media:.2f}")
print(f"🏆 Máximo: {maximo}")
print("-"*50)

print("⬛ Cuadrado de cada número:")
for n, c in zip(numeros, cuadrados):
    print(f"   {n:>8}  →  {c:.2f}")

print("-"*50)
if duplicados:
    print(f"⚠️  Duplicados encontrados: {sorted(duplicados)}")
else:
    print("✅ No hay duplicados.")
print("="*50)
