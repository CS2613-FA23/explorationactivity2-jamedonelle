import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QComboBox, QTextEdit, QFileDialog
from PyQt5.QtGui import QPixmap
import fitz
from deep_translator import GoogleTranslator

class PDFViewer(QMainWindow):
    def __init__(self, pdf_path, page_number):
        super().__init__()

        self.pdf_path = pdf_path
        self.page_number = page_number

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 1400, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel()
        self.layout.addWidget(self.label)

        # Side Menu
        self.side_menu_layout = QVBoxLayout()
        self.layout.addLayout(self.side_menu_layout)

        # Language Combo box
        self.language_combo_box = QComboBox()
        self.language_combo_box.addItems(["French", "English", "German", "Spanish"])
        self.language_combo_box.currentIndexChanged.connect(self.on_language_changed)
        self.side_menu_layout.addWidget(self.language_combo_box)

        # Page Combo Box
        self.page_combo_box = QComboBox()
        self.page_combo_box.currentIndexChanged.connect(self.on_index_changed)
        self.side_menu_layout.addWidget(self.page_combo_box)

        # Label and Line Edit for PDF File
        self.pdf_file_label = QLabel("PDF File:")
        self.pdf_file_line_edit = QLineEdit()
        self.pdf_file_line_edit.setReadOnly(True)

        self.pdf_file_layout = QHBoxLayout()
        self.pdf_file_layout.addWidget(self.pdf_file_label)
        self.pdf_file_layout.addWidget(self.pdf_file_line_edit)
        self.side_menu_layout.addLayout(self.pdf_file_layout)
        
        # Button to get file path
        self.pdf_button = QPushButton("...")
        self.pdf_button.clicked.connect(self.open_file_dialog)
        self.pdf_file_layout.addWidget(self.pdf_button)

        # QTextEdit
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.side_menu_layout.addWidget(self.text_edit)

    def render_pdf_page(self):
        image_path = f"./page-images/page-{self.page_number}.png"
        pdf_document = fitz.open(self.pdf_path)
        page = pdf_document.load_page(self.page_number - 1)

        if(not os.path.exists(image_path)): # we dont need to create the image since its already been generated
            # raster page
            pixmap = page.get_pixmap()
            pixmap.save(image_path)

        # get text from pdf page
        text = page.get_text()
        translated_text = GoogleTranslator(source='auto', target=self.language_combo_box.currentText().lower()).translate(text)
        self.text_edit.setText(translated_text)

        pdf_document.close()
        
        q_pixmap = QPixmap(image_path)  
        self.label.setPixmap(q_pixmap)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select PDF File", "", "PDF Files (*.pdf)")
        self.pdf_file_line_edit.setText(file_path)
        self.on_pdf_file_chosen()

    def populate_combo_box(self):
        pdf_document = fitz.open(self.pdf_path)
        number_of_pages = pdf_document.page_count
        pdf_document.close()

        for i in range(0, number_of_pages):
            self.page_combo_box.addItem(str(i + 1))

    def on_index_changed(self, index):
        selected_page = self.page_combo_box.itemText(index)
        self.page_number = int(selected_page)
        self.render_pdf_page()   

    def on_pdf_file_chosen(self):
        pdf_path = self.pdf_file_line_edit.text()
        if(os.path.exists(pdf_path)):
            page_image_dir = "./page-images/"
            page_images = os.listdir(page_image_dir)

            # Iterate through each file and delete
            for page in page_images:
                file_path = os.path.join(page_image_dir, page)
                if os.path.isfile(file_path):
                    os.remove(file_path)

            self.pdf_path = pdf_path
            self.populate_combo_box()
            self.render_pdf_page()

    def on_language_changed(self):
        text = self.text_edit.toPlainText()
        if text: # make sure its not empty
            translated_text = GoogleTranslator(source='auto', target=self.language_combo_box.currentText().lower()).translate(text)
            self.text_edit.setText(translated_text)


def main():
    pdf_file_path = ''
    page_to_display = 1  # Change this to the desired page number

    app = QApplication(sys.argv)
    pdf_viewer = PDFViewer(pdf_file_path, page_to_display)
    pdf_viewer.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()