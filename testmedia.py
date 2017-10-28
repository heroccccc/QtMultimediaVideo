from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        videoWidget = QVideoWidget()
        btn = QPushButton("play", self)
        btn2 = QPushButton("pause", self)
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(btn)
        layout.addWidget(btn2)
        wid = QWidget(self)
        wid.setLayout(layout)
        self.setCentralWidget(wid)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("/Users/hiroshi/py/video/1.mp4")))


        btn.clicked.connect(self.play)
        btn2.clicked.connect(self.pause)


    def play(self):
        self.mediaPlayer.play()

    def pause(self):
        self.mediaPlayer.pause()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = Window()
    player.resize(1200, 760)
    player.show()

    sys.exit(app.exec_())
