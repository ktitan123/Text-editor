import sys
import os
from PyQt4 import QtGui

class Notepad(QtGui.QMainWindow):
	def __init__(self):
		super(Notepad,self).__init__()
		self.initUI()
	
	def initUI(self):
		self.text=QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)
		exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)        
          	exitAction.setShortcut('Ctrl+Q')
        	exitAction.setStatusTip('Exit application')
        	exitAction.triggered.connect(QtGui.qApp.quit)
		
		newaction=QtGui.QAction('New',self)
		newaction.setShortcut('Ctrl+N')
		newaction.setStatusTip('Create new file')
		newaction.triggered.connect(self.newFile)
		
		saveaction=QtGui.QAction('Save',self)
		saveaction.setShortcut('Ctrl+S')
		saveaction.setStatusTip('Save file')
		saveaction.triggered.connect(self.saveFile)
		
		openaction=QtGui.QAction('Open',self)
		openaction.setShortcut('Ctrl+O')
		openaction.setStatusTip('Open file')
		openaction.triggered.connect(self.openFile)
		
		undoaction=QtGui.QAction('Undo',self)
		undoaction.setShortcut('Ctrl+Z')
		undoaction.setStatusTip('Undo last action')
		undoaction.triggered.connect(self.undoact)
		
		textcolor=QtGui.QAction('Text Color',self)
		textcolor.setStatusTip('Change the color of text')
		textcolor.triggered.connect(self.textcolorchange)
		
		
		italic=QtGui.QAction('It',self)
		italic.triggered.connect(self.italici)
		
		underline=QtGui.QAction('U',self)
		underline.triggered.connect(self.underline)
		
		#self.btn=QtGui.QPushButton('Dialog',self)
		#self.btn.move(60,10)
		#self.btn.clicked.connect(self.showDialog)
		
		
		
		
		self.statusBar().showMessage('Ready')
		self.toolbar=self.addToolBar('Italic')
		self.toolbar.addAction(italic)
		
		
		self.toolbar=self.addToolBar('Underline')
		self.toolbar.addAction(underline)
		
		menubar=self.menuBar()
		fileMenu=menubar.addMenu('&File')
		editmenu=menubar.addMenu('Edit')
		
		
		
		fileMenu.addAction(newaction)
		fileMenu.addAction(openaction)
		fileMenu.addAction(saveaction)
		fileMenu.addAction(exitAction)
		
		editmenu.addAction(undoaction)
		editmenu.addAction(textcolor)
		
		
		self.setGeometry(1000,300,300,300)
		self.setWindowTitle('Notepad')
		self.show()
	
	#font actions italic,underline etc
	
	def italici(self):
		if self.text.fontItalic()==False:
			self.text.setFontItalic(True)
		else:
			self.text.setFontItalic(False)
	
	def underline(self):
		if self.text.fontUnderline()==False:
			self.text.setFontUnderline(True)
		else:
			self.text.setFontUnderline(False)
		
	
	#def showDialog(self):
	#	text,ok=QtGui.QInputDialog.getText(self,'Input Dialog','Enter your name')
	#	if ok:
	#		self.text.setText(str(text))
	
	
	#************** EDIT MENU **********************************
	def undoact(self):
		self.text.undo()
	
	def textcolorchange(self):
		
	
	
	#**************FILE MENU*************************************
	
	def newFile(self):
		self.text.clear()
	
	def saveFile(self):
		filename=QtGui.QFileDialog.getSaveFileName(self,'Save File',os.getenv('HOME'))
		f=open(filename,'w')
		filedata=self.text.toPlainText()
		f.write(filedata)
		f.close()
		
	def openFile(self):
		filename=QtGui.QFileDialog.getOpenFileName(self,'Open File',os.getenv('HOME'))
		f=open(filename,'r')
		filedata=f.read()
		self.text.setText(filedata)
		f.close()
	
def main():	
	app = QtGui.QApplication(sys.argv)
	notepad=Notepad()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()
	
	



