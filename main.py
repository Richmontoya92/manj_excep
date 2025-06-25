# Importa la clase Foto del módulo foto
from foto import Foto
# Importa la excepción personalizada DimensionError del módulo error
from error import DimensionError

print("--- Prueba de la clase Foto y DimensionError ---")

# Prueba 1: Crear una foto con dimensiones válidas
try:
    print("\nCreando foto con dimensiones válidas (1024x768)...")
    foto1 = Foto(1024, 768, "path/to/foto1.jpg")
    print(f"Foto 1 creada: Ancho={foto1.ancho}, Alto={foto1.alto}")
except DimensionError as e:
    print(f"Error inesperado al crear foto1: {e}")
except Exception as e:
    print(f"Error general inesperado: {e}")

# Prueba 2: Intentar modificar el ancho con un valor inválido (menor a 1)
try:
    print("\nIntentando modificar ancho de foto1 a 0...")
    foto1.ancho = 0
except DimensionError as e:
    print(f"Error esperado al modificar ancho (valor 0): {e}")
except Exception as e:
    print(f"Error general inesperado: {e}")

# Prueba 3: Intentar modificar el alto con un valor inválido (mayor a MAX)
try:
    print("\nIntentando modificar alto de foto1 a 3000...")
    foto1.alto = 3000
except DimensionError as e:
    print(f"Error esperado al modificar alto (valor 3000): {e}")
except Exception as e:
    print(f"Error general inesperado: {e}")

# Prueba 4: Intentar modificar el ancho con un valor válido
try:
    print("\nIntentando modificar ancho de foto1 a 800 (válido)...")
    foto1.ancho = 800
    print(f"Ancho de foto1 modificado a: {foto1.ancho}")
except DimensionError as e:
    print(f"Error inesperado al modificar ancho (valor 800): {e}")
except Exception as e:
    print(f"Error general inesperado: {e}")

# Prueba 5: Crear una excepción DimensionError solo con mensaje
try:
    print("\nCreando DimensionError solo con mensaje...")
    raise DimensionError("Este es un error general de dimensión.")
except DimensionError as e:
    print(f"DimensionError (solo mensaje): {e}")

# Prueba 6: Crear una excepción DimensionError con mensaje y dimensión
try:
    print("\nCreando DimensionError con mensaje y dimensión...")
    raise DimensionError("Dimensión inválida.", dimension="Profundidad")
except DimensionError as e:
    print(f"DimensionError (mensaje y dimensión): {e}")

# Prueba 7: Crear una excepción DimensionError con todos los atributos
try:
    print("\nCreando DimensionError con todos los atributos...")
    raise DimensionError("El valor excede el máximo.", dimension="Peso", maximo=100)
except DimensionError as e:
    print(f"DimensionError (todos los atributos): {e}")

print("\n--- Fin de las pruebas ---")