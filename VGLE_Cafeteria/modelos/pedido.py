from modelos.cliente_frecuente import ClienteFrecuente

class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        subtotal = sum(p.get_precio() for p in self._productos)
        if isinstance(self._cliente, ClienteFrecuente):
            descuento = (subtotal * self._cliente.obtener_descuento()) / 100
            return subtotal - descuento
        return subtotal

    def __str__(self):
        nombres = ", ".join([p._nombre for p in self._productos])
        return f"Pedido de {self._cliente._nombre} | Productos: [{nombres}] | Total Final: ${self.calcular_total():.2f}"