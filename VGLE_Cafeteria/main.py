from modelos.cafeteria import Cafeteria
from modelos.cliente import Cliente
from modelos.cliente_frecuente import ClienteFrecuente
from modelos.producto import Producto
from controlador.gestor import GestorCafeteria

def ejecutar_sistema():
    mi_cafeteria = Cafeteria("Skywlkr Coffee Shop")
    gestor_ventas = GestorCafeteria(mi_cafeteria)

    prod1 = Producto("Americano", 45.0)
    prod2 = Producto("Capuchino", 65.0)
    prod3 = Producto("Panini de Pavo", 95.0)
    prod4 = Producto("Muffin de Chocolate", 40.0)
    
    for p in [prod1, prod2, prod3, prod4]:
        mi_cafeteria.registrar_producto(p)

    c1 = Cliente("Eduardo villeda", "N-101")
    c2 = Cliente("Isaac Villeda", "N-102")
    f1 = ClienteFrecuente("Dana Juárez", "F-501", 15)
    f2 = ClienteFrecuente("Yoselin Alduenda", "F-502", 25)
    
    for c in [c1, c2, f1, f2]:
        mi_cafeteria.registrar_cliente(c)

    gestor_ventas.realizar_venta("N-101", ["Americano", "Panini de Pavo"])
    gestor_ventas.realizar_venta("N-102", ["Capuchino", "Muffin de Chocolate"])
    gestor_ventas.realizar_venta("F-501", ["Capuchino", "Panini de Pavo"])
    gestor_ventas.realizar_venta("F-502", ["Americano", "Americano"])

    print(mi_cafeteria)
    print("\nREPORTE FINAL DE PEDIDOS:")
    print("-" * 50)
    for p in mi_cafeteria._pedidos:
        print(p)

if __name__ == "__main__":
    ejecutar_sistema()