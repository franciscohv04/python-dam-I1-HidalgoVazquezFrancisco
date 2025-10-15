# Programa: Resumen estadístico de calificaciones
# Autor: ChatGPT
# Descripción: Este programa solicita una lista de calificaciones al usuario
# y muestra un resumen estadístico (cantidad, media, mínimos, máximos, etc.),
# validando que todos los valores sean numéricos y estén en el rango 0–10.

from statistics import mean, multimode

# Solicitar al usuario una lista de calificaciones separadas por comas
entrada = input("Introduce las calificaciones separadas por comas (ejemplo: 6.5, 8, 5, 4, 9, 10, 7, 3): ")

try:
    # Convertir los valores a flotantes y eliminar espacios extra
    notas = [float(x.strip()) for x in entrada.split(",")]

    # Validar que todas las notas estén entre 0 y 10
    if any(n < 0 or n > 10 for n in notas):
        print("\nError: Todas las notas deben estar entre 0 y 10. Intenta de nuevo.")
    else:
        # Calcular estadísticas básicas
        total = len(notas)
        media = round(mean(notas), 2)
        minima = min(notas)
        maxima = max(notas)

        # Calcular porcentajes
        aprobados = sum(1 for n in notas if n >= 5)
        sobresalientes = sum(1 for n in notas if n >= 9)
        porc_aprob = (aprobados / total) * 100
        porc_sobresal = (sobresalientes / total) * 100

        # Calcular la moda (pueden ser varias)
        modas = multimode(notas)

        # Determinar mensaje final según la media
        if media >= 8:
            nivel = "Nivel excelente"
        elif media >= 5:
            nivel = "Nivel medio"
        else:
            nivel = "Necesita refuerzo"

        # Mostrar resultados
        print("\n--- RESUMEN ESTADÍSTICO ---")
        print(f"Total de notas: {total}")
        print(f"Media: {media}")
        print(f"Nota mínima: {minima}")
        print(f"Nota máxima: {maxima}")
        print(f"Porcentaje de aprobados: {porc_aprob:.2f}%")
        print(f"Porcentaje de sobresalientes: {porc_sobresal:.2f}%")
        print(f"Nota(s) más repetida(s): {', '.join(map(str, modas))}")
        print(f"Mensaje final: {nivel}")

except ValueError:
    print("\nError: Asegúrate de introducir solo números válidos separados por comas.")
