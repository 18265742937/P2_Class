from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import configparser
import random
import time
import sys
import os


class musicPlayer(QWidget):
	def __init__(self):
		super().__init__()
		self.__initialize()
	

	def __initialize(self):
		self.setWindowTitle('茄子音乐播放器')
		self.setWindowIcon(QIcon('icon.ico'))
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	gui = musicPlayer()
	gui.show()
	sys.exit(app.exec_())
