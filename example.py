import sys
import datetime
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QLabel, QWidget


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        self.name_label = QLabel("Enter name: ")
        self.name_input = QLineEdit()
        self.date_label = QLabel("Enter date of birth: ")
        self.date_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.output_label = QLabel("")

        self.setFixedWidth(400)
        self.setFixedHeight(150)

        grid.addWidget(self.name_label, 0, 0, 1, 1)
        grid.addWidget(self.name_input, 0, 1, 1, 3)
        grid.addWidget(self.date_label, 1, 0, 1, 1)
        grid.addWidget(self.date_input, 1, 1, 1, 3)
        grid.addWidget(self.submit_button, 2, 1, 1, 2)
        grid.addWidget(self.output_label, 3, 1, 1, 2)

        self.submit_button.clicked.connect(self.calculate_age)

        self.setLayout(grid)

    def calculate_age(self):
        print('Calculating age.')
        current_year = datetime.datetime.now()
        user_name = self.name_input.text()
        current_year_text = self.date_input.text()
        print(1)
        current_year_date = datetime.datetime.strptime(current_year_text, "%d/%m/%Y")
        print(current_year_date)
        age = current_year - current_year_date
        self.output_label.setText(f"{user_name} is {int(age.days / 365)} years old.")


application = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
application.exec()
