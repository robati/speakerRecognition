#test_gender.py
import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
from PyQt4 import QtCore,QtGui, uic
from PyQt4.QtGui import *
import sys
warnings.filterwarnings("ignore")
import time


#path to training data
source   = "development_set\\"   

modelpath = "speaker_models\\"

test_file = "development_set_test.txt"        

file_paths = open(test_file,'r')

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models    = [cPickle.load(open(fname,'r')) for fname in gmm_files]
speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]

# Read the test directory and get the list of test audio files 
'''for path in file_paths:
    print  path
    path = path.strip()   
    print path
    sr,audio = read(source + path)
    vector   = extract_features(audio,sr)
    
    log_likelihood = np.zeros(len(models)) 
    
    for i in range(len(models)):
        gmm    = models[i]         #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    
    winner = np.argmax(log_likelihood)
    print "\tdetected as - ", speakers[winner]
    time.sleep(1.0)'''

def findSpeacker(path):

    sr, audio = read(source + path)
    vector = extract_features(audio, sr)

    log_likelihood = np.zeros(len(models))

    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()

    winner = np.argmax(log_likelihood)
    return speakers[winner]



class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('test1.ui', self)
        self.pushButton.clicked.connect(self.browseFile)
        self.pushButton_2.clicked.connect(self.detect)
        self.pushButton_3.clicked.connect(self.submit)
        self.msg = QMessageBox()
        self.show()
        self.file = ""
        for i in range(len(speakers)):
            self.comboBox.addItem(speakers[i])


    def browseFile(self):
        self.file=QFileDialog.getOpenFileName()
        self.file=self.getFileName(self.file)
        #print "the"+self.file
        self.Filelabel.setText("~"+self.file)


    def detect(self):
        speaker = findSpeacker(self.file)
        #self.msg.setText("detected as - "+speaker)
        self.msg.setText(speaker)
        self.msg.exec_()

    def submit(self):
        selected_speaker = self.comboBox.currentText()
        speaker = findSpeacker(self.file)
        print ("!"+speaker+"! and-!" + selected_speaker+"!")
        verified = (str(selected_speaker) == str(speaker))
        self.msg.setText( str(verified))
        self.msg.exec_()

    def getFileName(self,path):
        i=path.split("development_set")
        if(len(i)==1):
            return i[0]
        return i[1]
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
