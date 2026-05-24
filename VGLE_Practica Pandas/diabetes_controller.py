import flet as ft
from diabetes_modelo import DiabetesModel

class DiabetesController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = DiabetesModel()

    # MOSTRAR ESTADÍSTICAS
    def mostrar_estadisticas(self, e):
        total = self.modelo.total_pacientes()
        glucosa = self.modelo.promedio_glucosa()
        diabetes = self.modelo.pacientes_diabetes()
        embarazos = self.modelo.promedio_embarazos_diabetes()
        
        # Llama a la nueva estadística
        edad_promedio = self.modelo.promedio_edad()
        
        self.vista.resultado.value = f"""Total pacientes: {total}
Promedio glucosa: {glucosa}
Pacientes con diabetes: {diabetes}
Promedio embarazos con diabetes: {embarazos}
Edad promedio general: {edad_promedio} años"""

        self.vista.page.update()

    # MOSTRAR PACIENTES DE RIESGO
    def mostrar_riesgo(self, e):
        self.vista.limpiar_tabla()
        riesgo = self.modelo.pacientes_riesgo()
        
        for _, fila in riesgo.iterrows():
            # Tarjetas con bordes y fondo usando texto plano para evitar errores
            tarjeta = ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Glucosa: {fila['Glucose']}", weight="bold"),
                        ft.Text(f"BMI: {fila['BMI']}"),
                        ft.Text(f"Edad: {fila['Age']}")
                    ]
                ),
                padding=10,
                border=ft.border.all(2, "red"),
                border_radius=10,
                bgcolor="black"
            )
            self.vista.tabla.controls.append(tarjeta)
        self.vista.page.update()