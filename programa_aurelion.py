import re
import os

def cargar_md(ruta_md):
    if not os.path.exists(ruta_md):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_md}")
    with open(ruta_md, "r", encoding="utf-8") as f:
        return f.read()

def extraer_secciones(markdown_texto):
    """Divide el contenido del Markdown según los títulos principales numerados (## 1), ## 2), etc.)."""
    patron = re.compile(r"(##\s*\d+\).*?)(?=##\s*\d+\)|\Z)", re.S)
    secciones = patron.findall(markdown_texto)
    estructura = {}
    for seccion in secciones:
        lineas = seccion.strip().split("\n", 1)
        titulo = lineas[0].replace("##", "").strip()
        contenido = lineas[1].strip() if len(lineas) > 1 else ""
        estructura[titulo] = contenido
    return estructura

def mostrar_menu(secciones):
    print("\n=== MENU AURELION ===\n")
    for i, titulo in enumerate(secciones.keys(), 1):
        print(f"{titulo}")
    print("0) Salir\n")

def main():
    ruta_md = "documentacion_aurelion.md"
    try:
        markdown_texto = cargar_md(ruta_md)
        secciones = extraer_secciones(markdown_texto)
    except FileNotFoundError as e:
        print(e)
        return

    while True:
        mostrar_menu(secciones)
        opcion = input("Selecciona una opcion: ")

        if opcion == "0":
            print("\nPrograma finalizado.")
            break

        if not opcion.isdigit() or int(opcion) not in range(1, len(secciones) + 1):
            print("Opcion invalida. Intenta de nuevo.\n")
            continue

        clave = list(secciones.keys())[int(opcion) - 1]
        print(f"\n--- {clave} ---\n")
        print(secciones[clave])
        print("\n--- Fin de la seccion ---\n")
        input("Presiona 'Enter' para volver al menu principal")

if __name__ == "__main__":
    main()
