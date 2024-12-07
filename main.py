import ctypes
import sys
import os

from PyQt6.QtWidgets import QApplication, QStyleFactory
from PyQt6.QtGui import QIcon

from photo_processor import PhotoID_Processor

try:
    myappid = 'com.d-110.PhotoID-Processor.v0.1.0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
icon_path = os.path.join(base_path, 'main-icon.png')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))
    app.setApplicationName("PhotoID Processor")
    app.setStyle(QStyleFactory.create('Fusion'))
    
    window = PhotoID_Processor()
    window.setWindowTitle("PhotoID Processor")
    window.show()
    sys.exit(app.exec())

