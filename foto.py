# Importa la excepción personalizada DimensionError del módulo error
from error import DimensionError

# Definición de la clase Foto
class Foto():
    # Atributo de clase que define el valor máximo permitido para ancho y alto
    MAX = 2500

    # Constructor de la clase Foto
    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        # Inicializa los atributos privados __ancho y __alto
        # No se realiza validación aquí, ya que la validación se hace en los setters
        self.__ancho = ancho
        self.__alto = alto
        self.ruta = ruta # Asigna la ruta, que no es un atributo privado en el original

    # Propiedad para obtener el ancho de la foto
    @property
    def ancho(self) -> int:
        return self.__ancho

    # Setter para el ancho de la foto con validación
    @ancho.setter
    def ancho(self, ancho) -> None:
        # Valida que el ancho esté dentro del rango permitido (1 a MAX)
        if not (1 <= ancho <= Foto.MAX):
            # Lanza una excepción DimensionError si el valor no es válido
            raise DimensionError(f"El ancho {ancho} está fuera del rango permitido.",
                                 dimension="Ancho", maximo=Foto.MAX)
        # Si el valor es válido, asigna el nuevo ancho
        self.__ancho = ancho

    # Propiedad para obtener el alto de la foto
    @property
    def alto(self) -> int:
        return self.__alto

    # Setter para el alto de la foto con validación
    @alto.setter
    def alto(self, alto) -> None:
        # Valida que el alto esté dentro del rango permitido (1 a MAX)
        if not (1 <= alto <= Foto.MAX):
            # Lanza una excepción DimensionError si el valor no es válido
            raise DimensionError(f"El alto {alto} está fuera del rango permitido.",
                                 dimension="Alto", maximo=Foto.MAX)
        # Si el valor es válido, asigna el nuevo alto
        self.__alto = alto