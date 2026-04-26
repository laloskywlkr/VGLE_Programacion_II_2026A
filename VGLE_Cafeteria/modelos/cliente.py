class Cliente:
    def __init__(self, nombre, id_cliente):
        self._nombre = nombre
        self._id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self._nombre} (ID: {self._id_cliente})"