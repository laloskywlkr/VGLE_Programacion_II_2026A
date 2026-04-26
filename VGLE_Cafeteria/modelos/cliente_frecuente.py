from modelos.cliente import Cliente

class ClienteFrecuente(Cliente):
    def __init__(self, nombre, id_cliente, descuento=15):
        super().__init__(nombre, id_cliente)
        self._descuento = descuento

    def obtener_descuento(self):
        return self._descuento

    def __str__(self):
        return f"Cliente Frecuente: {self._nombre} (ID: {self._id_cliente}) - Descuento: {self._descuento}%"