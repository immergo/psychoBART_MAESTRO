from BARTBalloon import *
from BARTFixationCross import *
from BARTSummarySceen import *
from BARTGui import *
from psychopy.constants import NOT_STARTED, STARTED, FINISHED
from psychopy.tools.monitorunittools import pix2deg, deg2pix
import random
from psychopy import core

class BARTObject:
    def __init__(self, win,mon):
        self.status = NOT_STARTED
        self.tStart = None
        self.frameNStart = None
        self.win = win
        self.mon = mon
        self.currentBaloon = None
        self.fixationCross = BARTFixationCross(self.win)
        self.gui = BARTGui(self.win,self.mon)
        self.totalNumberOfPumps = 0
        self.balloonNumberOfPumps = 0
        self.totalPoints = 0
        self.balloonPoints = 0
        self.summaryScreen = None

    def makeBalloon(self, balloonID='niebieski', color=(255, 255, 255), maxPumps=128, gainpoints=1, initsize=(1, 1), gainsize=1, mon=0):
        self.currentBaloon = BARTBalloon(self.win, balloonID, color, maxPumps, gainpoints, initsize, gainsize, mon)

    def pumpBalloonImg(self):
        self.currentBaloon.pumpSound.play()

        self.currentBaloon.stimuli.size = [x + self.currentBaloon.gainSize for x in self.currentBaloon.stimuli.size]
        self.currentBaloon.stimuli.pos = self.currentBaloon.updateBalloonPos()
        self.balloonNumberOfPumps += 1

        explosion = random.random() * (self.currentBaloon.maxPumps - self.balloonNumberOfPumps)
        # based on the other paper: return (this.rand>Math.pow(me.prob-me.pump, -1))?false:true;

        if explosion < 1:
            self.balloonPoints = 0
            self.explode()
        else:
            self.balloonPoints += 1

    def pumpBalloon(self):
        self.currentBaloon.stimuli.radius = [x + self.currentBaloon.gainSize for x in self.currentBaloon.stimuli.radius]

        self.balloonNumberOfPumps += 1

        explosion = random.random() * (self.currentBaloon.maxPumps - self.balloonNumberOfPumps)
        # based on the other paper: return (this.rand>Math.pow(me.prob-me.pump, -1))?false:true;

        if explosion < 1:
            self.balloonPoints = 0
            self.explode()
        else:
            self.balloonPoints += 1

    def start(self):
        self.balloonPoints = 0
        self.balloonNumberOfPumps = 0
        self.status = STARTED

    def complete(self):
        self.status = FINISHED

    def explode(self):
        self.status = 'EXPLODE'

    def showSummary(self):
        self.summaryScreen = BARTSummaryScreen(self.win)
        self.summaryScreen.updateMarkerPosition(self.balloonNumberOfPumps, self.currentBaloon.maxPumps)
        self.summaryScreen.draw()