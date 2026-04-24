from figuras.cuadrado import Cuadrado
from figuras.circulo import Circulo
from figuras.triangulo import Triangulo

def menu():
    while True:
        print("\n--- CALCULADORA DE FIGURAS ---")
        print("1. Cuadrado")
        print("2. Círculo")
        print("3. Triángulo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            l = float(input("Lado del cuadrado: "))
            fig = Cuadrado(l)
        elif opcion == "2":
            r = float(input("Radio del círculo: "))
            fig = Circulo(r)
        elif opcion == "3":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            l1 = float(input("Lado 1: "))
            l2 = float(input("Lado 2: "))
            l3 = float(input("Lado 3: "))
            fig = Triangulo(b, h, l1, l2, l3)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
            continue

        print(f"\nResultado para {type(fig).__name__}:")
        print(f"Área: {fig.area():.2f}")
        print(f"Perímetro: {fig.perimetro():.2f}")

if __name__ == "__main__":
    menu()