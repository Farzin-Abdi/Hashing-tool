import sys
import base64
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel, QComboBox, QCheckBox
import hashlib

class HashingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hashing & Encoding Tool')
        self.setGeometry(200, 200, 600, 400)  # Set initial size and position

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Enter your text here")
        self.input_field.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.input_field.textChanged.connect(self.auto_update)
        self.layout.addWidget(self.input_field)

        self.options_layout = QHBoxLayout()
        self.layout.addLayout(self.options_layout)

        self.method_selection = QComboBox()
        self.method_selection.addItems([
            'SHA256',
            'SHA1',
            'SHA224',
            'SHA384',
            'SHA512',
            'SHA3_256',
            'SHA3_512',
            'MD5',
            'Base64'
        ])
        self.method_selection.currentIndexChanged.connect(self.update_ui)
        self.method_selection.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.options_layout.addWidget(self.method_selection)

        self.auto_update_checkbox = QCheckBox("Auto Update")
        self.auto_update_checkbox.setChecked(True)
        self.auto_update_checkbox.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.options_layout.addWidget(self.auto_update_checkbox)

        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)
        self.output_field.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.layout.addWidget(self.output_field)

        self.execute_button = QPushButton('Execute')
        self.execute_button.clicked.connect(self.execute_method)
        self.execute_button.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.layout.addWidget(self.execute_button)

        self.decode_button = QPushButton('Decode Base64')
        self.decode_button.clicked.connect(self.decode_base64)
        self.decode_button.setStyleSheet("""
            font-size: 18px;
            padding: 10px;
        """)
        self.layout.addWidget(self.decode_button)

        self.update_ui()  # Update the UI to reflect the initial state

    def update_ui(self):
        if self.method_selection.currentText() == 'Base64':
            self.decode_button.show()
        else:
            self.decode_button.hide()

    def execute_method(self):
        self.update_output()

    def decode_base64(self):
        input_data = self.input_field.toPlainText()

        try:
            output = base64.b64decode(input_data).decode()
        except Exception as e:
            output = "Invalid Base64 string."

        self.output_field.setText(output)

    def auto_update(self):
        if self.auto_update_checkbox.isChecked():
            self.update_output()

    def update_output(self):
        input_data = self.input_field.toPlainText().encode()
        method = self.method_selection.currentText()

        if method == 'Base64':
            output = base64.b64encode(input_data).decode()
        else:
            hash_object = getattr(hashlib, method.lower())(input_data)
            output = hash_object.hexdigest()

        self.output_field.setText(output)

def main():
    app = QApplication(sys.argv)

    hashing_app = HashingApp()
    hashing_app.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

