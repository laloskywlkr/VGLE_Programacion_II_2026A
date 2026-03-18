from modelos.libro import Libro
from modelos.usuarios import Usuario
from servicios.gestorprestamos import GestorPrestamos

libro1=Libro("The Martian", "Andy Weir", "12345")
usuario1=Usuario("Lalo", "2011201")

gestor=GestorPrestamos()
mensaje=gestor.realizarPrestamo(libro1, usuario1, "070326")
print(mensaje)
print(libro1.getDisponibilidad())
gestor.listarPrestamo()
#print(libro1._titulo) sin proteccion
print(libro1.getTitulo())

libro2=Libro("Harry Potter", "J K Rowlling", "12345")
print(libro1==libro2)

print(usuario1)