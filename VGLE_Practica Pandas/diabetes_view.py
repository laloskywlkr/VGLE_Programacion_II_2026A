import flet as ft

class DiabetesView:
    def __init__(self, page: ft.Page):
        self.page = page
        # CONFIGURACIÓN Y DISEÑO VISUAL
        self.page.title = "Análisis Dataset Diabetes"
        self.page.window_width = 850
        self.page.window_height = 750
        self.page.padding = 25
        self.page.theme_mode = ft.ThemeMode.DARK  # Modo oscuro activado
        
        # BOTONES CON NUEVO DISEÑO (Colores estándar en texto plano)
        self.btn_estadisticas = ft.ElevatedButton(
            "Mostrar estadísticas",
            bgcolor="blue",
            color="white"
        )
        
        self.btn_riesgo = ft.ElevatedButton(
            "Pacientes de riesgo",
            bgcolor="red",
            color="white"
        )
        
        # RESULTADOS
        self.resultado = ft.Text(size=18, color="green", weight="medium")
        
        # Fila con scroll automático para las tarjetas de riesgo
        self.tabla = ft.Row(wrap=True, spacing=10, scroll=ft.ScrollMode.AUTO)

    # CONSTRUIR INTERFAZ
    def construir(self):
        return ft.Column(
            controls=[
                ft.Text(
                    "Sistema de Análisis Diabetes",
                    size=32,
                    weight="bold",
                    color="blue"
                ),
                ft.Divider(color="blue"),
                ft.Row(
                    controls=[self.btn_estadisticas, self.btn_riesgo],
                    alignment=ft.MainAxisAlignment.START
                ),
                ft.Divider(color="blue"),
                self.resultado,
                ft.Text("Resultados de Riesgo:", size=16, weight="bold"),
                ft.Container(content=self.tabla, height=300)  # Contenedor para evitar desbordamientos
            ],
            spacing=20
        )

    # LIMPIAR TABLA
    def limpiar_tabla(self):
        self.tabla.controls.clear()