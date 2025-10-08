# 📘 Analizador de texto con manejo de errores de números

print("="*60)
print("🔤  ANALIZADOR DE CADENA DE TEXTO MEJORADO")
print("="*60)

try:
    # Pedir al usuario una cadena
    texto = input("Introduce una cadena de texto: ").strip()

    # Comprobar si el usuario no ingresó texto
    if not texto:
        print("⚠️  No se ingresó ninguna cadena. Por favor escribe algo.")
        exit()

    # Comprobar si la cadena contiene al menos una letra
    if not any(c.isalpha() for c in texto):
        print("⚠️  La cadena debe contener al menos una letra. No se aceptan solo números o símbolos.")
        exit()

    # Inicializar contadores
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    num_vocales = 0
    num_consonantes = 0
    num_mayusculas = 0
    num_minusculas = 0
    num_caracteres = len(texto)
    num_palabras = len(texto.split())

    # Recorrer cada carácter en el texto
    for c in texto:
        if c.isalpha():  # Solo letras
            if c in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
            if c.isupper():
                num_mayusculas += 1
            elif c.islower():
                num_minusculas += 1

    # Mostrar resultados
    print("\n" + "-"*60)
    print("📊  RESULTADOS DEL ANÁLISIS")
    print("-"*60)
    print(f"🔡 Vocales:         {num_vocales}")
    print(f"🅱️ Consonantes:     {num_consonantes}")
    print(f"🔠 Mayúsculas:      {num_mayusculas}")
    print(f"🔡 Minúsculas:      {num_minusculas}")
    print(f"🔢 Caracteres totales: {num_caracteres}")
    print(f"📝 Palabras:        {num_palabras}")
    print("-"*60)
    print("✅ Análisis completado con éxito.")
    print("="*60)

except Exception as e:
    print("\n⚠️  Error inesperado:", e)
    print("   Asegúrate de escribir una cadena de texto válida.")


