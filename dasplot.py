# -*- coding: utf-8 -*-
"""
Created on Wed Dec 05 10:40:42 2012
This program should create a simple qt plot which data cna be pushed to
@author: keyan
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplot
import sys, os, random, time
import Queue

from livedatafeed import LiveDataFeed

class graph(matplot.Ui_MainWindow,QMainWindow):
    def __init__(self,parent=None):
        
        super(graph, self).__init__(parent)
        self.setupUi(self)
                
        # Initialize some variables
        self.monitor_active = False
        self.x = [0]
        self.y = [0]
        
        self.livedata = LiveDataFeed()
        self.data_q = Queue.Queue
        
        # Set up the Axes
        self.axes = self.mplwidget.figure.add_subplot(111)
        self.axes.hold(False)
        
        # GUI update timer
        timer = QTimer(self)
        QObject.connect(timer, SIGNAL("timeout()"), self.update_figure)
        timer.start(1000)
        
    def start(self):
        
    def plotdata(self,xdata,ydata):
        self.x = xdata
        self.y = ydata
    
    def acquiredata(self):
        for i in range(1,100):
            time.sleep(1)
            self.x.append(i)
            self.y.append(i)
        
    def update_figure(self):
        x = self.x
        y = self.y
        self.axes.plot(x,y,'r')
        self.mplwidget.draw()
        self.show()