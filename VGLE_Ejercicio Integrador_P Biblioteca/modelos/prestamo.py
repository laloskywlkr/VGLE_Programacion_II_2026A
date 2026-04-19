class Prestamo:
    def __init__(self,libro,usuario,fechaprestamo):
        self.__usuario = usuario
        self.__libro = libro
        self.__fechaprestamo = fechaprestamo
                
    def getUsuario(self):
        return self.__usuario

    def getLibro(self):
        return self.__libro
    
    def getFechaPrestamo(self):
        return self.__fechaprestamo
        
    def __str__(self):
        return f"Usurio: {self.__usuario} -- Libro: {self.__libro}"