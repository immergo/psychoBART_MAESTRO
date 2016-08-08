from psychopy import prefs
prefs.general['audioLib'] = ['pyo']
from psychopy import sound
from psychopy import visual
from psychopy.tools.monitorunittools import pix2deg, deg2pix

class BARTBalloon:
    def __init__(self, win, balloonID, color, maxPumps, gainpoints, initsize, gainsize, mon):
        self.win = win
        self.balloonID = balloonID
        self.color = color
        self.maxPumps = maxPumps
        self.points = gainsize
        self.initSize = initsize  # units 'deg'
        self.initSizeX = 3.5
        self.initSizeY = 5
        self.gainSize = gainsize  # units 'deg'
        self.mon = mon
        self.pump = visual.ImageStim(win, image="assets/pump.png", pos=[0, 0], size=[10, 10])
        self.explosionSound = sound.Sound(value='assets\explode.wav')
        self.explosionSound.setVolume(1.0)
        self.pumpSound = sound.Sound(value='assets\pump4.wav')
        self.pumpSound.setVolume(1.0)

        self.pump.pos = [0, pix2deg(-690 + (deg2pix(self.pump.size[1], mon) / 2), mon)]
        self.stimuli = visual.ImageStim(win, image="assets/bal_blue.png", pos=[0,pix2deg(-400+(deg2pix(self.initSizeY,mon)/2),mon)],size=[self.initSizeX,self.initSizeY])

        #self.stimuli = visual.Circle(self.win, radius=self.initSize, edges=512, lineColor=self.color, fillColor=self.color)

    def updateBalloonPos(self):
        return [0, pix2deg(-400 + (deg2pix(self.stimuli.size[1], self.mon) / 2), self.mon)]