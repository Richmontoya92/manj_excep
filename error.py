# Definición de la clase de excepción personalizada DimensionError
class DimensionError(Exception):
    # Constructor de la excepción DimensionError
    # Recibe mensaje, dimension (opcional) y maximo (opcional)
    def __init__(self, mensaje: str, dimension: str = None, maximo: int = None) -> None:
        # Llama al constructor de la clase base Exception
        super().__init__(mensaje)
        # Asigna los atributos de instancia
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    # Sobrecarga del método __str__ para personalizar el mensaje de la excepción
    def __str__(self) -> str:
        # Si solo se proporcionó el mensaje, retorna el mensaje de la clase padre
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        # Si se proporcionaron atributos adicionales, construye un mensaje personalizado
        else:
            msg = f"{self.mensaje}"
            if self.dimension:
                msg += f" Dimensión: {self.dimension}."
            if self.maximo:
                msg += f" Máximo permitido: {self.maximo}."
            return msg