class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo=titulo
        self.__autor=autor
        self.__isbn=isbn
        self.__disponibilidad=True

    def prestar(self):
        if (self.__disponibilidad):
            self.__disponibilidad=False
            return True;
        return False
    
    def devolver(self):
        self.__disponibilidad=True
        
    def getTitulo(self):
        return self.__titulo
    
    def getDisponibilidad(self):
        return self.__disponibilidad
    
    def __str__(self):
        return f"{self.__titulo}"

    def __repr__(self):
        return f"Libro('{self.__titulo}', '{self.__autor}')"
    
    def __eq__(self, otrolib):
        return self.__titulo == otrolib.__titulo
    


  