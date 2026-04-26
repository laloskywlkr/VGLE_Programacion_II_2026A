class Cafeteria:
    def __init__(self, nombre):
        self._nombre = nombre
        self._clientes = []
        self._productos = []
        self._pedidos = []

    def registrar_cliente(self, cliente):
        self._clientes.append(cliente)

    def registrar_producto(self, producto):
        self._productos.append(producto)

    def registrar_pedido(self, pedido):
        self._pedidos.append(pedido)

    def __str__(self):
        return f"--- {self._nombre} ---"