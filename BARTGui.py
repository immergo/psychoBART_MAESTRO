# -*- coding: utf-8 -*-

from psychopy import visual
from psychopy.tools.monitorunittools import pix2deg, deg2pix

class BARTGui:
    def __init__(self, win, mon):
        self.lastScoreText = u'Ostatnia wygrana: '
        self.totalScoreText = u'Całkowita wygrana: '
        self.lastScore = visual.TextStim(win, text=self.lastScoreText, units='deg', pos=(20,-12), color=u'black')
        self.totalScore = visual.TextStim(win, text=self.totalScoreText, units='deg', pos=(20.3,-13.5), color=u'black')

        self.keyPump = visual.ImageStim(win, image="assets/key_up.png", pos=[-12,-12],size=[pix2deg(128,mon),pix2deg(128,mon)])
        self.keyCollect = visual.ImageStim(win, image="assets/key_enter.png", pos=[-20,-12],size=[pix2deg(128,mon),pix2deg(128,mon)])
        self.keyPumpLabel = visual.TextStim(win, text=u'DMUCHNIJ', units='deg', pos=(-12,-15), color='#404040')
        self.keyCollectLabel = visual.TextStim(win, text=u'ZAKOŃCZ', units='deg', pos=(-20,-15), color='#404040')

    def draw(self):
        self.lastScore.draw()
        self.totalScore.draw()
        self.keyPump.draw()
        self.keyCollect.draw()
        self.keyPumpLabel.draw()
        self.keyCollectLabel.draw()

    def update(self, last, total):
        self.lastScore.text = self.lastScoreText + str(last)
        self.totalScore.text = self.totalScoreText + str(total)