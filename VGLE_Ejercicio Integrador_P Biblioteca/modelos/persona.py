class Persona:
    def __init__(self,nombre,identificador):
        self.__nombre = nombre
        self.__identificador = identificador
        
    def getNombre(self):
        return self.__nombre
    
    def getIdentificador(self):
        return self.__identificador
    
    def mostrardatos(self):
        return f"{self.__nombre} - {self.__identificador}"
        
    def __str__(self):
        return f"{self.__nombre} - {self.__identificador}"