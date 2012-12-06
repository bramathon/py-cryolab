# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 10:40:42 2012
This program should create a simple qt plot which data cna be pushed to
@author: keyan
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplot
import sys, os, random

class graph(matplot.Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        print "Called setupUi"
        self.axes = self.mplwidget.figure.add_subplot(111)
        self.axes.hold(False)
        print "Created self.axes"
        timer = QTimer(self)
        QObject.connect(timer, SIGNAL("timeout()"), self.update_figure)
        timer.start(1000)
        
    def plotdata(self,xdata,ydata):
        self.x = xdata
        self.y = ydata
        
    def update_figure(self):
        l = [ random.randint(0, 10) for i in range(4) ]
        self.axes.plot([0,1,2,3],l,'r')
        self.mplwidget.draw()
        self.show()