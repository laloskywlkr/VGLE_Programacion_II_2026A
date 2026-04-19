from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.Gestor_Prestamos import GestorPrestamos
from modelos.biblioteca import Biblioteca
from modelos.bibliotecario import Bibliotecario
from modelos.alumno import Alumno

#Crear biblioteca
biblioteca1 = Biblioteca("Biblioteca Central")

#crear bibliotecario
bibliotecario1 = Bibliotecario("Carlos","B001","IA")

#crear libro
libro1 = Libro("Peppa Pig","Bucanero",)
libro2 = Libro("Teoria de Evolucion del Ser Humano","Jorge el Salvaje")

#Bibliotecario registra libros
bibliotecario1.registrar_libro(biblioteca1,libro1)
bibliotecario1.registrar_libro(biblioteca1,libro2)

#Libros disponibles
biblioteca1.listar_libros()

#crear usuario
alumno1=Alumno("Eduardo","A001","Alumno")

#Crear Gestor de prestamos
gestor=GestorPrestamos()

#Realizaar prestamo
gestor.realizar_prestamo(libro1,alumno1,"18-04-2026")

#Imprimir prestamos
gestor.listar_prestamos()


print(bibliotecario1.descripcion())
print(alumno1.descripcion())