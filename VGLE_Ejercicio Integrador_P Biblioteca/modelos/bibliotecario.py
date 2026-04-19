from modelos.usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self,nombre,identificador,area):
        super().__init__(nombre,identificador,"Bibliotecario")
        self._area = area

    def obtener_area(self):
        return self._area
        
    def registrar_libro(self,biblioteca,libro):
        biblioteca.agregar_libros(libro)
        print(f"{self.getNombre()} registro el libro {libro.getTitulo()}")

    def descripcion(self):
        return f"El bibliotecario del Area: {self._area}"