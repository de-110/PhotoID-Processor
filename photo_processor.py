import sys
import os

from PyQt6.QtWidgets import QMainWindow, QFileDialog

from docx.shared import Inches
from docx import Document

desktop = os.path.join(os.path.expanduser("~"))

class PhotoID_Processor(QMainWindow):
    def __init__(self):
        super().__init__()

        document = Document()
        self.open_file()

    def open_file(self):
        print("open file")
        selected_file = self.open_dialog('open_file')
        print(selected_file)
    
    def process_file(self):
        print("process file")

    def save_file(self):
        print("save file")
        selected_file = self.open_dialog('save_file')
        print(selected_file)
        
    def open_dialog(self, mode):
        dialog = QFileDialog(self)

        match mode:
            case 'open_file':
                filename, _ = dialog.getOpenFileName(
                    self,
                    "Open File",
                    desktop,
                    "Images (*.png *.jpg)"
                )
                return filename
            
            case 'save_file':
                filename, _ = dialog.getSaveFileName(
                    self,
                    "Save File",
                    desktop,
                    "Word Documents (*.docx)"
                )
                return filename