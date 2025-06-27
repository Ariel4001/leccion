from PySide6.QtCore import QDateTime, QDate
from PySide6.QtWidgets import QMainWindow, QMessageBox

from src.UI.vtnActividad import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBorrar.clicked.connect(self.borrar)


    def guardar(self):
        nombre = self.ui.txtNombre.text().strip()
        apellido = self.ui.txtApellido.text().strip()
        fecha_seleccionada = self.ui.dtFecha.dateTime()
        duracion_str = self.ui.txtDuracion.text().strip()
        tipo_actividad = self.ui.cbTipoActividad.currentText()
        if not nombre:
            QMessageBox.warning(self, "Error de Validación", "El campo nombre no puede estar vacío.")
            return

        if not apellido:
            QMessageBox.warning(self, "Error de Validación", "El campo apellido no puede estar vacío.")
            return

        if not duracion_str:
            QMessageBox.warning(self, "Error de Validación", "El campo duracion no puede estar vacío.")
            return
        try:
            duracion = float(duracion_str)
            if duracion <= 0:
                QMessageBox.warning(self, "Error de Validación",
                                    "La 'Duración' debe ser un valor numérico positivo.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error de Validación",
                                "El campo duracion debe ser un valor numérico válido.")
            return


        if tipo_actividad == "Seleccionar":
            QMessageBox.warning(self, "Error de Validación",
                                "Por favor, seleccione un 'Tipo de Actividad' válido.")
            return


        fecha_actual = QDateTime.currentDateTime()

        limite_inferior_fecha = QDate(2020, 1, 1)


        if fecha_seleccionada > fecha_actual:
            QMessageBox.warning(self, "Error de Validación",
                                "La fecha de la actividad no puede ser en el futuro.")
            return

        if fecha_seleccionada.date() < limite_inferior_fecha:
            QMessageBox.warning(self, "Error de Validación",
                                f"La fecha de la actividad no puede ser anterior al {limite_inferior_fecha.toString('dd/MM/yyyy')}.")
            return

        print(f"Actividad validada y lista para guardar:")
        print(f"  Nombre: {nombre}")
        print(f"  Apellido: {apellido}")
        print(f"  Fecha: {fecha_seleccionada.toString('dd/MM/yyyy HH:mm')}")
        print(f"  Duración: {duracion} horas")
        print(f"  Tipo de Actividad: {tipo_actividad}")

        QMessageBox.information(self, "Éxito", "Actividad guardada correctamente.")
        self.borrar()
        self.ui.statusbar.showMessage('GRACIAS POR USAR NUESTRO SISTEMA', 5000)
        self.borrar()

    def borrar(self):
            self.ui.txtNombre.clear()
            self.ui.txtApellido.clear()
            self.ui.txtDuracion.clear()
            self.ui.dtFecha.setDateTime(QDateTime.currentDateTime())
            self.ui.cbTipoActividad.setCurrentIndex(0)



