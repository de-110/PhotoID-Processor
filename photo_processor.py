import sys
import os

from PyQt6.QtWidgets import QMainWindow

from docx.shared import Inches
from docx import Document


class PhotoID_Processor(QMainWindow):
    def __init__(self):
        super().__init__()

        document = Document()

    def open_file(self):
        print("open file")
    
    def process_file(self):
        print("process file")

    def save_file(self):
        print("save file")