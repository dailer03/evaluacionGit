def validar_prueba(valor):
    """Algoritmo básico para una prueba de validación."""
    if valor is None or valor == "":
        return "Prueba no válida: valor vacío"
    return "Prueba válida"


if __name__ == "__main__":
    print(validar_prueba("EPS"))
    print(validar_prueba(""))
