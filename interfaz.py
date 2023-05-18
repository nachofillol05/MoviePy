from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap
import sys
from moviepy.editor import *

class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MoviePy Video Editor")
        self.setGeometry(100, 100, 1100, 150)
        
        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(50, 50, 100, 30)
        self.save_button.clicked.connect(self.save_video)
        
        self.title_button = QPushButton("Add Title", self)
        self.title_button.setGeometry(350, 50, 100, 30)
        self.title_button.clicked.connect(self.add_title)
        
        self.volume_button = QPushButton("Volume", self)
        self.volume_button.setGeometry(950, 50, 100, 30)
        self.volume_button.clicked.connect(self.open_volume_dialog)
                
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(200, 50, 100, 30)
        self.open_button.clicked.connect(self.open_file_dialog)

        self.open_button = QPushButton("Add Clip", self)
        self.open_button.setGeometry(800, 50, 100, 30)
        self.open_button.clicked.connect(self.open_clip_dialog)
        
        self.label_ubicacion = QLabel(self)
        self.label_ubicacion.setText("Ingrese la ruta del archivo")
        self.label_ubicacion.setGeometry(150, 20, 500, 30)
        
        self.label_duracion = QLabel(self)
        self.label_duracion.setText("")
        self.label_duracion.setGeometry(200, 75, 500, 30)
        
        self.label_finalizado = QLabel(self)
        self.label_finalizado.setText("")
        self.label_finalizado.setGeometry(200, 100, 500, 30)
                    
        self.rotate_button = QPushButton("Rotate", self)
        self.rotate_button.setGeometry(500, 50, 100, 30)
        self.rotate_button.clicked.connect(self.rotate)
        
        self.rotate_button = QPushButton("Hacer gif", self)
        self.rotate_button.setGeometry(650, 50, 100, 30)
        self.rotate_button.clicked.connect(self.gif)
        
        self.video = None
    
    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.file_path = file_dialog.selectedFiles()[0]
            self.video = VideoFileClip(self.file_path)
            self.label_ubicacion.setText(self.file_path)
            self.label_duracion.setText("El video dura: " + str(self.video.duration) + " segundos")

    def open_clip_dialog(self):
        if self.video is not None:
            self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Video Files (*.mp4 *.avi)")
            if file_dialog.exec_() == QFileDialog.Accepted:
                file_path = file_dialog.selectedFiles()[0]
                self.clip = VideoFileClip(file_path)
                self.video = concatenate_videoclips([self.video,self.clip])
            
    '''def open_route_file(self):
        file_dialog = QFileDialog(self)
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.guardado_archivo = file_dialog.selectFile()
            self.label_ubicacion.setText(self.guardado_archivo)'''
            
    def add_title(self):
        
        text = TextClip("LinuxHint", fontsize=75, color = "white")
        text2 = text.set_pos("center").set_duration(3)

        self.video = CompositeVideoClip([self.video, text2])
        video2.write_videofile("texted.mp4")
        
        
        """
        
        if self.video is not None:
            title_text, ok = QInputDialog.getText(self, "Add Title", "Enter Title Text:")
            if ok:
                title_clip = TextClip(title_text, fontsize=70, color='white')
                video_with_title = CompositeVideoClip([self.video, title_clip.set_pos(('center', 'top'))])
                self.video = video_with_title
                self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
                """
    
    def gif(self):
        self.label_finalizado.setText("Procesando video...")
        self.video.write_gif("gif.gif")
        self.label_finalizado.setText("Se termino de guardar el video")
    
    def rotate(self):
        grados = 0
        if self.video is not None:
            try:
                resultado = QInputDialog.getText(self, "Rotate", "Cuantos grados:(Numero porfavor)")#es ua tupla
                grados = int(resultado[0])
                
            except ValueError:
                print("Ingrese un numero")
            if grados != 0:
                print("lklegueeeeeeeee")
                self.video = self.video.rotate(grados)
                
    def save_video(self):
        self.label_finalizado.setText("Procesando el video...")
        if self.video is not None:
            self.video.write_videofile("jose.mp4")
            self.label_finalizado.setText("Se termino de guardar el video")

    def open_volume_dialog(self):
        if self.video is not None:
            volume, ok = QInputDialog.getText(self, "Change Volume", "Enter New Volume:")
            if ok:
                self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
                self.videovolume = self.video.volumex(volume)
                self.video = self.videovolume


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = VideoEditor()
    editor.show()
    sys.exit(app.exec_())
    