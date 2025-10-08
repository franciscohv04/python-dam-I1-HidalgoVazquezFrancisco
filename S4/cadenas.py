# 📘 Analizador de texto: cuenta vocales, consonantes, mayúsculas y caracteres

print("="*50)
print("🔤  ANALIZADOR DE CADENA DE TEXTO")
print("="*50)

# Pedir al usuario una cadena
texto = input("Introduce una cadena de texto: ")

# Definir vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Inicializar contadores
num_vocales = 0
num_consonantes = 0
num_mayusculas = 0
num_caracteres = len(texto)

# Recorrer cada carácter en el texto
for c in texto:
    if c.isalpha():  # Solo letras
        if c in vocales:
            num_vocales += 1
        else:
            num_consonantes += 1
    if c.isupper():
        num_mayusculas += 1

# Mostrar resultados con formato
print("\n" + "-"*50)
print("📊  RESULTADOS DEL ANÁLISIS")
print("-"*50)
print(f"🔡 Vocales:        {num_vocales}")
print(f"🅱️ Consonantes:    {num_consonantes}")
print(f"🔠 Mayúsculas:     {num_mayusculas}")
print(f"🔢 Caracteres totales: {num_caracteres}")
print("-"*50)
print("✅ Análisis completado con éxito.")
print("="*50)
