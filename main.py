import random
import sys
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generate_button.clicked.connect(self.generate_password)
        self.ui.ok_button.clicked.connect(self.check_data)
        self.show()
        self.password = ""

    def generate_password(self):
        if self.ui.letter_size_check.isChecked() and self.ui.number_check.isChecked() and self.ui.special_check.isChecked():
            password_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+")
        elif self.ui.letter_size_check.isChecked() and self.ui.number_check.isChecked():
            password_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        elif self.ui.number_check.isChecked() and self.ui.special_check.isChecked():
            password_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+")
        elif self.ui.special_check.isChecked() and self.ui.letter_size_check.isChecked():
            password_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+")
        else:
            password_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        try:
            password_length = int(self.ui.letter_number_edit.text())
            self.password = "".join(random.choice(password_letters) for _ in range(password_length))
            message = QMessageBox()
            message.setText(self.password)
            message.exec()
        except ValueError:
            message = QMessageBox()
            message.setText("Podaj długość hasła")
            message.exec()
    def check_data(self):
        name = self.ui.name_edit.text()
        last_name = self.ui.lastname_edit.text()
        position = self.ui.position_combo.currentText()

        if name and last_name:
            message = QMessageBox()
            message.setText(name + " " + last_name + " " + position + " " + self.password)
            message.exec()
        else:
            message = QMessageBox()
            message.setText("Coś poszło nie tak")
            message.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
