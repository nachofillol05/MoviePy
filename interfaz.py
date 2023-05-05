from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap
import sys
from moviepy.editor import *
import os
os.environ["IMAGEIO_CONVERTER"] = r"/home/nacho/Descargas/magick"  # reemplaza la ruta con la ubicación real del binario de ImageMagick



class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MoviePy Video Editor")
        self.setGeometry(100, 100, 800, 600)


class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MoviePy Video Editor")
        self.setGeometry(100, 100, 800, 600)
        
        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(50, 50, 100, 30)
        self.play_button.clicked.connect(self.play_video)
        
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(200, 50, 100, 30)
        self.open_button.clicked.connect(self.open_file_dialog)


class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MoviePy Video Editor")
        self.setGeometry(100, 100, 800, 600)
        
        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(50, 50, 100, 30)
        self.play_button.clicked.connect(self.play_video)
        
        self.title_button = QPushButton("Add Title", self)
        self.title_button.setGeometry(350, 50, 100, 30)
        self.title_button.clicked.connect(self.add_title)
        
                
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(200, 50, 100, 30)
        self.open_button.clicked.connect(self.open_file_dialog)
        
        self.video_widget = QLabel(self)
        self.video_widget.setGeometry(50, 100, 700, 400)
        self.video_widget.setStyleSheet("border: 1px solid black")
        
        self.video_widget = QLabel(self)
        self.video_widget.setGeometry(50, 100, 700, 400)
        self.video_widget.setStyleSheet("border: 1px solid black")
        
        self.video = None
    
    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            self.video = VideoFileClip(file_path)
            
    def add_title(self):
        if self.video is not None:
            title_text, ok = QInputDialog.getText(self, "Add Title", "Enter Title Text:")
            if ok:
                title_clip = TextClip(title_text, fontsize=70, color='white')
                video_with_title = CompositeVideoClip([self.video, title_clip.set_pos(('center', 'top'))])
                self.video = video_with_title
    
    def play_video(self):
        if self.video is not None:
            self.video.preview()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = VideoEditor()
    editor.show()
    sys.exit(app.exec_())
