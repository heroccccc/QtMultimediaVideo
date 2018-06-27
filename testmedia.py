from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        videoWidget = QVideoWidget()

        #2つボタンを設置
        btn = QPushButton("play", self)
        btn2 = QPushButton("pause", self)

        #全体のレイアウト設定
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(btn)
        layout.addWidget(btn2)

        #ビデオ再生部分の設定
        wid = QWidget(self)
        wid.setLayout(layout)
        self.setCentralWidget(wid)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoWidget)

        #絶対パスで再生したいファイルを指定
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("***********************")))

        #設置したボタンを押した際のメソッドを指定
        btn.clicked.connect(self.play)
        btn2.clicked.connect(self.pause)

    #再生
    def play(self):
        self.mediaPlayer.play()

    #停止
    def pause(self):
        self.mediaPlayer.pause()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = Window()

    #ディスプレイの大きさを取得
    screen = app.desktop()
    height = screen.height()
    width = screen.width()

    #スクリーンいっぱいに表示
    player.resize(width,height)
    player.show()

    sys.exit(app.exec_())
