import sys
import os

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap, QIntValidator
from PyQt6.QtCore import Qt
from PyQt6 import uic

from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches
from docx import Document

desktop = os.path.join(os.path.expanduser("~"))

photo_processor_ui, classinfo = uic.loadUiType('photo_processor.ui')

class PhotoID_Processor(QMainWindow, photo_processor_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
        self.document = Document()

        self.selected_file = None

        self.set_img_path()

        self.id_type.addItems(['','2x2', '1x1'])

        self.browse_button.clicked.connect(self.open_file)
        self.process_button.clicked.connect(self.handle_file)
    
    def set_img_path(self):
        if not self.selected_file:
            self.img_path.setText(desktop)
        else:
            self.img_path.setText(self.selected_file)

    def open_file(self):
        self.selected_file = self.open_dialog('open_file')
        self.preview_image()
        self.set_img_path()
    
    def handle_file(self):
        id_type = self.id_type.currentText()
        num_of_photos = self.num_of_photos.text()

        if not self.selected_file:
            print('please select a photo to process!!')
        if not num_of_photos:
            print('please input how many photos to process!!')

        else:
            match id_type:
                case '2x2':                    
                    self.create_photoID(2, num_of_photos, self.selected_file, id_type)

                case '1x1':
                    self.create_photoID(1, num_of_photos, self.selected_file, id_type)
                
                case '':
                    print('please select and id type!!')

    def create_photoID(self, size, num_of_photos, selected_file, id_type):
        photos = int(num_of_photos)
        counter = 0
        
        p = self.document.add_paragraph()
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        r = p.add_run()
        
        for id in range(photos):
            counter += 1
            
            r.add_picture(selected_file, width=Inches(size), height=Inches(size))
            match (counter, id_type):
                case (2, '2x2'):
                    r.add_break()
                    counter = 0
                case (4, '1x1'):
                    r.add_break()
                    counter = 0

        self.save_file()

    def save_file(self):
        print("save file")
        try:
            save_to = self.open_dialog('save_file')
            self.document.save(save_to)
        except FileNotFoundError:
            return
    
    def preview_image(self):
        pixmap = QPixmap(self.selected_file)
        scaled_pixmap = pixmap.scaled(self.preview_img.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.preview_img.setPixmap(scaled_pixmap)
        
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