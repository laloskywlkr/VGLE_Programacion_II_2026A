class Libro:
    def __init__(self,titulo,autor):
        self._titulo = titulo
        self._autor = autor
        self._disponibilidad = True 
    
    def getTitulo(self):
        return self._titulo

    def getDisponibilidad(self):
        return self._disponibilidad
            
    def prestar(self):
        if (self._disponibilidad):
            self._disponibilidad = False
            return True
        return False
    
    def devolver(self):
        self._disponibilidad = True

    def __str__(self):
        return f"{self._titulo}"

    def __eq__(self, other):
        if not (other, Libro):
            return False
        return self._titulo == other._titulo