import sys
import os

from PyQt6.QtWidgets import QApplication, QStyleFactory
from photo_processor import PhotoID_Processor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("PhotoID Processor")
    app.setStyle(QStyleFactory.create('Fusion'))
    
    window = PhotoID_Processor()
    window.show()
    sys.exit(app.exec())

