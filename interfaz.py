from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
from moviepy.editor import *


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
        
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(200, 50, 100, 30)
        self.open_button.clicked.connect(self.open_file_dialog)
        
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
    
    def play_video(self):
        if self.video is not None:
            self.video.preview()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = VideoEditor()
    editor.show()
    sys.exit(app.exec_())
