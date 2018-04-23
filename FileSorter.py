import sys
import os
import os.path as path
import pathlib
import shutil
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

def sortFiles(directoryPath):
	files = os.listdir(directoryPath)
	for currentFile in files:
		fname, fextn = path.splitext(currentFile)
		pathlib.Path(directoryPath+ '\\' +fextn.strip('.')).mkdir(parents = True, exist_ok = True)
		if os.path.isfile(directoryPath+ '\\' + currentFile) and not (os.path.isfile(directoryPath+ '\\' + fextn.strip('.')+ '\\' + currentFile)):
			shutil.move(directoryPath+ '\\'+currentFile, directoryPath+ '\\'+fextn.strip('.'))

def createUI():
	#Create window using QT
	app = QApplication([])
	widget = QWidget()
	widget.setWindowTitle('FileSorter')

	#create label
	label = QLabel('Please input the directory path', widget)

	#Create Textbox
	textbox = QLineEdit(widget)
	textbox.move(10, 40)
	textbox.resize(280, 40)

	widget.resize(320, 150)

	# Create a button in the window
	button = QPushButton('Sort', widget)
	button.move(20,100)

	@pyqtSlot()
	def on_click():
		dirPath = textbox.text()
		dirPath = str(dirPath)
		sortFiles(dirPath)
		label = QLabel('finish', widget)

	button.clicked.connect(on_click)
	widget.show()
	app.exec_()

createUI()