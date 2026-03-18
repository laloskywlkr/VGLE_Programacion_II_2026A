class Prestamo:
    def __init__(self, usuario, libro, fecha):
        self.__usuario=usuario
        self.__libro=libro
        self.__fecha=fecha

    def getUsuario(self):
        return self.__usuario
    
    def getLibro(self):
        return self.__libro
    
    def getFecha(self):
        return self.__fecha
    
    def __str__(self):
        return f"{self.__fecha}"
    
    def __str__(self):
        return f"{self.__usuario} - {self.__libro}"
    
