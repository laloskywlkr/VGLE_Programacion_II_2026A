from modelos.libro import Libro
from modelos.prestamo import Prestamo 

class GestorPrestamos:
    def __init__(self):
        self.prestamos = []
    
    def realizar_prestamo(self,libro,usuario,fecha):
        if libro.getDisponibilidad():
            libro.prestar()
            prestamo = Prestamo(libro,usuario,fecha)
            self.prestamos.append(prestamo)
            return "Prestamo realizado correctamente" 
        return "El libro no esta disponible"
    
    def listar_prestamos(self):
        if not self.prestamos:
            print("No hay prstamos")
        for prestamo in self.prestamos:
            print(prestamo)