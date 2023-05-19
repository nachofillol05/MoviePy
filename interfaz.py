from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QInputDialog
from PyQt5.QtGui import QPixmap
import sys
from moviepy.editor import *

class VideoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MoviePy Video Editor")
        self.setGeometry(100, 100, 650, 670)
        
        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(50, 100, 100, 30)
        self.save_button.clicked.connect(self.save_video)
        
        self.volume_button = QPushButton("Volume", self)
        self.volume_button.setGeometry(50, 400, 100, 30)
        self.volume_button.clicked.connect(self.open_volume_dialog)

        self.newaudio_button = QPushButton("Set Audio", self)
        self.newaudio_button.setGeometry(200, 400, 100, 30)
        self.newaudio_button.clicked.connect(self.change_audio)

        self.audiont_button = QPushButton("Remove Audio", self)
        self.audiont_button.setGeometry(350, 400, 100, 30)
        self.audiont_button.clicked.connect(self.remove_audio)
                
        self.open_button = QPushButton("Open", self)
        self.open_button.setGeometry(200, 100, 100, 30)
        self.open_button.clicked.connect(self.open_file_dialog)

        self.open_button = QPushButton("Add Clip", self)
        self.open_button.setGeometry(350, 100, 100, 30)
        self.open_button.clicked.connect(self.open_clip_dialog)

        self.rotate_button = QPushButton("Rotate", self)
        self.rotate_button.setGeometry(50, 260, 100, 30)
        self.rotate_button.clicked.connect(self.rotate)

        self.resize_button = QPushButton("Resize", self)
        self.resize_button.setGeometry(200, 260, 100, 30)
        self.resize_button.clicked.connect(self.resize)

        self.cut_button = QPushButton("Cut", self)
        self.cut_button.setGeometry(50, 550, 100, 30)
        self.cut_button.clicked.connect(self.cut)

        self.accelerate_button = QPushButton("Accelerate", self)
        self.accelerate_button.setGeometry(200, 550, 100, 30)
        self.accelerate_button.clicked.connect(self.accelerate)
        
        self.rotate_button = QPushButton("Make gif", self)
        self.rotate_button.setGeometry(500, 100, 100, 30)
        self.rotate_button.clicked.connect(self.gif)
        
        self.label_ubicacion = QLabel(self)
        self.label_ubicacion.setText("Ingrese la ruta del archivo")
        self.label_ubicacion.setGeometry(0, 10, 600, 30)
        
        self.label_duracion = QLabel(self)
        self.label_duracion.setText("")
        self.label_duracion.setGeometry(0, 600, 500, 30)
        
        self.label_archivo = QLabel(self)
        self.label_archivo.setText("Archivo")
        self.label_archivo.setGeometry(0, 43, 500, 30)

        self.label_tamaño = QLabel(self)
        self.label_tamaño.setText("Tamaño, Duración y Rotación")
        self.label_tamaño.setGeometry(0, 195, 500, 30)

        self.label_audio = QLabel(self)
        self.label_audio.setText("Audio")
        self.label_audio.setGeometry(0, 343, 500, 30)

        self.label_audio = QLabel(self)
        self.label_audio.setText("Duración")
        self.label_audio.setGeometry(0, 498, 500, 30)

        self.label_linea4 = QLabel(self)
        self.label_linea4.setText("________________________________________________________________________________________")
        self.label_linea4.setGeometry(0, 475, 650, 30)

        self.label_linea1 = QLabel(self)
        self.label_linea1.setText("________________________________________________________________________________________")
        self.label_linea1.setGeometry(0, 25, 650, 30)

        self.label_linea2 = QLabel(self)
        self.label_linea2.setText("________________________________________________________________________________________")
        self.label_linea2.setGeometry(0, 175, 650, 30)

        self.label_linea3 = QLabel(self)
        self.label_linea3.setText("________________________________________________________________________________________")
        self.label_linea3.setGeometry(0, 325, 650, 30)

        self.label_finalizado = QLabel(self)
        self.label_finalizado.setText("")
        self.label_finalizado.setGeometry(0, 625, 650, 30)
        
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
    
    def gif(self):
        if self.video is not None:
            self.label_finalizado.setText("Procesando video...")
            self.video.write_gif("gif.gif")
            self.label_finalizado.setText("Se termino de guardar el video")
    
    def rotate(self):
        grados = 0
        if self.video is not None:
            try:
                resultado = QInputDialog.getText(self, "Rotate", "Cuantos grados:(Numero porfavor)")#es ua tupla
                grados = int(resultado[0])
                self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
                
            except ValueError:
                print("Ingrese un numero")
            if grados != 0:
                print("lklegueeeeeeeee")
                self.video = self.video.rotate(grados)

    def cut(self):
        if self.video is not None:
            print("xd")

    def accelerate(self):
        if self.video is not None:
            try:
                resultado = QInputDialog.getText(self, "Accelerating", "¿Por cuanto quieres acelerar el video?")
                aceleracion = float(resultado[0])

            except ValueError:
                pass
            self.video = self.video.fx(vfx.speedx, aceleracion)
            self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")

    def resize(self):
        if self.video is not None:
            try:
                resultado = QInputDialog.getText(self, "Resizing", "¿A cuánto quieres modificar el tamaño del video?(Ingrese el Ancho)")
                ancho = int(resultado[0])

            except ValueError:
                pass
            self.video = self.video.fx(vfx.resize, width = ancho)
            self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
                
    def save_video(self):
        if self.video is not None:
            self.label_finalizado.setText("Procesando el video...")
            if self.video is not None:
                self.video.write_videofile("jose.mp4")
                self.label_finalizado.setText("Se termino de guardar el video")

    def open_volume_dialog(self):
        if self.video is not None:
            try:
                volm, ok = QInputDialog.getText(self, "Change Volume", "Enter New Volume:")
                if ok:
                    self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
                    self.video = self.video.volumex(int(volm))
            except ValueError:
                print("Ingrese un numero")
                
    def remove_audio(self):
        if self.video is not None:
            self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")
            self.video = self.video.without_audio()

    def change_audio(self):
        if self.video is not None:
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Audio Files (*.wav *.mp3)")
            if file_dialog.exec_() == QFileDialog.Accepted:
                self.file_path = file_dialog.selectedFiles()[0]
                self.audio = AudioFileClip(self.file_path)
                self.video = self.video.set_audio(self.audio)
                self.label_finalizado.setText("NO CIERRE LA APLICACION O LOS CAMBIOS SERAN PERDIDOS")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = VideoEditor()
    editor.show()
    sys.exit(app.exec_())
    