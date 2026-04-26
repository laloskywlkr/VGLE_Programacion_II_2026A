from modelos.pedido import Pedido

class GestorCafeteria:
    def __init__(self, cafeteria_obj):
        self._cafeteria = cafeteria_obj

    def buscar_cliente(self, id_cliente):
        for c in self._cafeteria._clientes:
            if c._id_cliente == id_cliente:
                return c
        return None

    def buscar_producto(self, nombre_producto):
        for p in self._cafeteria._productos:
            if p._nombre.lower() == nombre_producto.lower():
                return p
        return None

    def realizar_venta(self, id_cliente, lista_productos):
        cliente = self.buscar_cliente(id_cliente)
        if not cliente:
            print(f"Error: No existe el cliente con ID {id_cliente}")
            return None
        
        nuevo_pedido = Pedido(cliente)
        for nombre in lista_productos:
            prod = self.buscar_producto(nombre)
            if prod:
                nuevo_pedido.agregar_producto(prod)
        
        self._cafeteria.registrar_pedido(nuevo_pedido)
        return nuevo_pedido