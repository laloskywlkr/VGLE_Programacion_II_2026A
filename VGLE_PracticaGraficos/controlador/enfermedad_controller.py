import flet as ft
import matplotlib.pyplot as plt
from modelo.enfermedad_model import EnfermedadModel


class EnfermedadController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = EnfermedadModel()

    def mostrar_estadisticas(self, e):
        total = self.modelo.total_pacientes()
        glucosa = self.modelo.promedio_glucosa()
        bmi = self.modelo.promedio_bmi()
        diabetes = self.modelo.pacientes_diabetes()
        sanos = self.modelo.pacientes_sanos()

        self.vista.resultado.value = f"""
Total pacientes: {total}

Promedio glucosa: {glucosa:.2f}

Promedio BMI: {bmi:.2f}

Pacientes con diabetes: {diabetes}

Pacientes sanos: {sanos}
"""

        self.vista.page.update()

        datos = [diabetes, sanos]
        etiquetas = ["Diabetes", "Sanos"]

        plt.pie(datos, labels=etiquetas, autopct="%1.1f%%")
        plt.title("Pacientes con y sin diabetes")
        plt.show()

    def mostrar_riesgo(self, e):
        self.vista.tabla.rows.clear()

        datos = self.modelo.pacientes_riesgo()

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(fila["Glucose"]))),
                        ft.DataCell(ft.Text(str(fila["BMI"]))),
                        ft.DataCell(ft.Text(str(fila["Age"]))),
                        ft.DataCell(ft.Text(str(fila["Outcome"]))),
                    ]
                )
            )

        self.vista.resultado.value = "Pacientes con alto riesgo:"
        self.vista.page.update()

    def mostrar_mayores(self, e):
        self.vista.tabla.rows.clear()

        datos = self.modelo.pacientes_mayores()

        for _, fila in datos.iterrows():
            self.vista.tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(fila["Glucose"]))),
                        ft.DataCell(ft.Text(str(fila["BMI"]))),
                        ft.DataCell(ft.Text(str(fila["Age"]))),
                        ft.DataCell(ft.Text(str(fila["Outcome"]))),
                    ]
                )
            )

        self.vista.resultado.value = "Pacientes mayores de 50 años:"
        self.vista.page.update()

    def mostrar_grafica_barras(self, e):
        diabetes = self.modelo.pacientes_diabetes()
        sanos = self.modelo.pacientes_sanos()

        etiquetas = ["Diabetes", "Sanos"]
        datos = [diabetes, sanos]

        plt.bar(etiquetas, datos)
        plt.title("Comparación de pacientes")
        plt.xlabel("Tipo de paciente")
        plt.ylabel("Cantidad")
        plt.show()