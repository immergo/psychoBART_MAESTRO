#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division
from psychopy import visual

class BARTSummaryScreen:
    def __init__(self, win):
        self.scoreLine = visual.Line(win, start=(-20,0), end=(20,0), lineColor='white')
        self.scoreLineLimitLeft = visual.Line(win, start=(-20,1), end=(-20,-1), lineColor='white')
        self.scoreLineLimitRight = visual.Line(win, start=(20,1), end=(20,-1), lineColor='white')
        self.scoreMarker = visual.Circle(win, radius=0.5, edges=32, fillColor='DarkSlateBlue')

    def updateMarkerPosition(self, balloonNumberOfPumps, balloonMaxPumps):
        distanceProportion = balloonNumberOfPumps/balloonMaxPumps
        self.scoreMarker.pos = ((40*distanceProportion)-20,0)

    def draw(self):
        self.scoreLine.draw()
        self.scoreLineLimitLeft.draw()
        self.scoreLineLimitRight.draw()
        self.scoreMarker.draw()
