import pandas as pd

class DiabetesModel:
    def __init__(self):
        # LEER DATASET
        self.df = pd.read_csv("C:/Users/lalov/Downloads/diabetes.csv")

    # TOTAL DE PACIENTES
    def total_pacientes(self):
        return len(self.df)

    # PROMEDIO DE GLUCOSA
    def promedio_glucosa(self):
        return round(self.df["Glucose"].mean(), 2)

    # PACIENTES CON DIABETES
    def pacientes_diabetes(self):
        return len(self.df[self.df["Outcome"] == 1])

    # PROMEDIO DE EMBARAZOS
    def promedio_embarazos_diabetes(self):
        diabetes = self.df[self.df["Outcome"] == 1]
        return round(diabetes["Pregnancies"].mean(), 2)

    # NUEVA ESTADÍSTICA: PROMEDIO DE EDAD DE PACIENTES
    def promedio_edad(self):
        return round(self.df["Age"].mean(), 1)

    # PACIENTES DE ALTO RIESGO MODIFICADO
    def pacientes_riesgo(self):
        # CAMBIO: Glucosa mayor a 180 y BMI mayor a 40
        riesgo = self.df[
            (self.df["Glucose"] > 180) & 
            (self.df["BMI"] > 40)
        ]
        # CAMBIO: Muestra más registros (subió de 10 a 20)
        return riesgo.head(20)