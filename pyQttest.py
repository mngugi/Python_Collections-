import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel # type: ignore
import warnings

warnings.filterwarnings("ignore")
def main():
   # Create the application instance
   app = QApplication(sys.argv)

   # Create the main window
   window = QMainWindow()
   window.setWindowTitle("Simple PyQt Example")
   window.setGeometry(100, 100, 400, 200)

   # Create a label widget
   label = QLabel("Hello, PyQt!", window)
   label.move(150, 80)

   # Show the window
   window.show()

   # Execute the application
   sys.exit(app.exec())

if __name__ == "__main__":
   main()