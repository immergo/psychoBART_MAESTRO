from psychopy import visual

class BARTFixationCross:
    def __init__(self, win):
        self.hLine = visual.Rect(win, width=1, height=0.125, units='deg', lineColor=u'black', fillColor=u'black')
        self.vLine = visual.Rect(win, width=0.125, height=1, units='deg', lineColor=u'black', fillColor=u'black')

    def draw(self):
        self.hLine.draw()
        self.vLine.draw()
