from modelos.usuario import Usuario

class Alumno(Usuario):
    def __init__(self,nombre,identificador,tipo_usuario):
        super().__init__(nombre,identificador,tipo_usuario)
        
    def pedirLibro(self):
         print("El alumno solicita un libro")

    def descripcion(self):
        return f"Alumno: {self.getNombre()}"