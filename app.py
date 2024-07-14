from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
# Змінна приложение
app = QApplication([])
# Створюемо вікно
window = QWidget()
window.resize(500, 300)
window.setWindowTitle("Generator")
#  Текст ( Лабел )
winner_lbl = QLabel('Натисни щоб дізнатися переможця')
num_lbl = QLabel('?')
btn_generate = QPushButton('Згенерувати')
# Віджети
vl = QVBoxLayout()
vl.addWidget(winner_lbl, alignment=Qt.AlignCenter)
vl.addWidget(num_lbl, alignment=Qt.AlignCenter)
vl.addWidget(btn_generate, alignment=Qt.AlignCenter)
window.setLayout(vl)




window.show()
app.exec_()
