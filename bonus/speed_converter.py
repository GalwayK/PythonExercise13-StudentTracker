from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QApplication, QDialog
from PyQt6.QtCore import QSize
import sys


class DistanceConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()

        self.setWindowTitle("Distance Converter")

        self.distance_label = QLabel("Distance: ")
        self.distance_entry = QLineEdit()

        self.time_label = QLabel("Time (hours): ")
        self.time_entry = QLineEdit()

        self.submit_button = QPushButton("Submit")

        self.converted_label = QLabel()

        self.unit_dropbox = QComboBox()
        self.unit_dropbox.addItem("Metric (miles)", userData="Metric")
        self.unit_dropbox.addItem("Imperial (Kilometers)", userData="Imperial")

        self.grid.addWidget(self.distance_label, 0, 0)
        self.grid.addWidget(self.distance_entry, 0, 1, 1, 2)
        self.grid.addWidget(self.unit_dropbox, 0, 3, 1, 1)
        self.grid.addWidget(self.time_label, 1, 0)
        self.grid.addWidget(self.time_entry, 1, 1, 1, 2)
        self.grid.addWidget(self.submit_button, 2, 0, 1, 3)
        self.grid.addWidget(self.converted_label, 3, 0, 1, 3)

        self.setLayout(self.grid)

        self.submit_button.clicked.connect(self.convert_distance)

    def convert_distance(self):
        try:
            distance = float(self.distance_entry.text())
            time = float(self.time_entry.text())
            data = distance / time
            if self.unit_dropbox.currentData() == "Metric":
                converted_data = data / 1.609
                self.converted_label.setText(f"You have travelled at {converted_data:.2f} miles per hour.")
            elif self.unit_dropbox.currentData() == "Imperial":
                converted_data = data * 1.609
                self.converted_label.setText(f"You have travelled at {converted_data:.2f} kilometers per hour.")
        except Exception as error:
            dlg = self.ErrorDialog()
            dlg.exec()

    class ErrorDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.grid = QGridLayout()

            self.error_label = QLabel("Error: Please enter valid data.")

            self.grid.addWidget(self.error_label, 0, 0)

            self.setWindowTitle("Error!")
            self.setLayout(self.grid)
            print("Why won't this work.")


app = QApplication(sys.argv)
window = DistanceConverter()
window.show()
app.exec()
