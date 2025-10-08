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

# Mostrar resultados
print(f"\nResultados:")
print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Máximo: {maximo}")
if duplicados:
    print(f"Duplicados encontrados: {sorted(duplicados)}")
else:
    print("No hay duplicados.")
