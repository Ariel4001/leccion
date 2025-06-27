import sys

from PySide6.QtWidgets import QApplication

from src.servicio.actividades import MyMainWindow

app = QApplication(sys.argv)
vtn_Actividad = MyMainWindow()
vtn_Actividad.show()
sys.exit(app.exec())