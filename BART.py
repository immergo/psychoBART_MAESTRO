#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui, monitors, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding
from ctypes import windll

from KeyResponseService import *
from BARTController import *

# notatki:
# - dodać instrukcję
# - dodac Blisko / Daleko
# - dodać informacje o postępie na ekran po prawej
# - inf. zw. tylko w bezpiecznych
# - dodać możliwość pompowania długich i krótkich balonów w jednym - losowo/blok? (6 x 5 bloków, w każdej piątce losujemy z poziomu)
# - feedback graficzny do balonów i chickengame, w balonach pokazujemy maksymalny rozmiar balonu
# - dzwiek: https://www.youtube.com/watch?v=Rz1OXrbCEtE
# Ostatnia wygrana: --
# Całkowita wygrana: 0 zł
# - CTRL i SPACJA wyswietlone
# - rozwalona opona / rozwalony balon | cala opona / caly balon

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'BART'  # from the Builder filename that created this script
expInfo = {'Participant ID':'',  'distance in cm':'57', 'monitor width in cm':'52', 'monitor resolution as [x,y]':'[1920,1080]'}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if not dlg.OK:
    core.quit()  # user pressed cancel

expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['Participant ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'D:\\home\\mskorko\\pythondev\\psychoBART\\BART.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
port = parallel.ParallelPort(address=0xB010)

# global io
# io = windll.inpout32
# print io
# adres fizyczny ltp
# marker = 0xB010
# io.Out32(marker,0)

# Setup the Monitor & Window
mon = monitors.Monitor('Main')
mon.setDistance(52)
mon.setWidth(57)
mon.setSizePix([1920,1080])

win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=mon, color=[0,0,0], colorSpace='rgb', units='deg',
    blendMode='avg', useFBO=True)

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
text1 = visual.TextStim(win=win, ori=0, name='text1',
                        text=u'W zadaniu można zdobyć punkty poprzez nadmuchiwanie balonów.\n\nW każdej rundzie tego zadania możesz nadmuchać prezentowany na ekranie balon naciskając klawisz: "STRZAŁKA DO GÓRY". Za każdym naciśnięciem klawisza otrzymujesz 1 punkt na tymczasowe konto.\n\nALE UWAŻAJ! Każdy balon możesz nadmuchać tylko określoną liczbę razy, zanim nie pęknie. Jeśli nadmuchasz balon za dużo razy, wybuchnie. Jeżeli balon pęknie, utracisz wygraną, która została zebrana od momentu rozpoczęcia danej próby na tymczasowym koncie.\n\nJeśli stwierdzisz, że nie chcesz dalej pompować danego balonika, naciśnij klawisz "ENTER". W tym przypadku wygrana z tymczasowego konta zostanie przeniesiona na stałe konto.\n\nTwoim zadaniem będzie napompować łącznie 30 balonów. Jeżeli balon pęknie lub przerwiesz pompowanie, przejdziesz automatycznie do kolejnego balonu.\n\n\n\n Naciśnij SPACJĘ by przejść do zadania',
                        font=u'Arial', pos=[0, 0], height=1, wrapWidth=50, color=u'white', colorSpace='rgb',
                        opacity=1,
                        depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
BARTObj = BARTObject(win,mon)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

###################################################################################

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
# update component parameters for each repeat
instr1_key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instr1_key_resp.status = NOT_STARTED
# keep track of which components have finished
instr1Components = []
instr1Components.append(text1)
instr1Components.append(instr1_key_resp)
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text1* updates
    if t >= 0.0 and text1.status == NOT_STARTED:
        # keep track of start time/frame for later
        text1.tStart = t  # underestimates by a little under one frame
        text1.frameNStart = frameN  # exact frame index
        text1.setAutoDraw(True)

    # *instr1_key_resp* updates
    if t >= 0.0 and instr1_key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1_key_resp.tStart = t  # underestimates by a little under one frame
        instr1_key_resp.frameNStart = frameN  # exact frame index
        instr1_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instr1_key_resp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instr1_key_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instr1_key_resp.keys = theseKeys[-1]  # just the last key pressed
            instr1_key_resp.rt = instr1_key_resp.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instr1_key_resp.keys in ['', [], None]:  # No response was made
    instr1_key_resp.keys = None
# store data for thisExp (ExperimentHandler)
thisExp.addData('instr1_key_resp.keys', instr1_key_resp.keys)
if instr1_key_resp.keys != None:  # we had a response
    thisExp.addData('instr1_key_resp.rt', instr1_key_resp.rt)
thisExp.nextEntry()
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

###################################################################################

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'BARTTrials.xlsx'),
    seed=None, name='trials')

thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)

    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    port.setData(0)

    # update component parameters for each repeat
    key_PUMP = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_PUMP.status = NOT_STARTED
    key_COLLECT = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_COLLECT.status = NOT_STARTED

    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(key_PUMP)
    trialComponents.append(key_COLLECT)
    trialComponents.append(BARTObj)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *key_PUMP* updates
        if frameN >= 150 and key_PUMP.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_PUMP.tStart = t  # underestimates by a little under one frame
            key_PUMP.frameNStart = frameN  # exact frame index
            key_PUMP.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_PUMP.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_PUMP.status == STARTED:
            theseKeys = event.getKeys(keyList=['up'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_PUMP.keys.extend(theseKeys)  # storing all keys
                key_PUMP.rt.append(key_PUMP.clock.getTime())
                if BARTObj.status == STARTED:
                    BARTObj.pumpBalloonImg()

        # *key_COLLECT* updates
        if frameN >= 150 and key_COLLECT.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_COLLECT.tStart = t  # underestimates by a little under one frame
            key_COLLECT.frameNStart = frameN  # exact frame index
            key_COLLECT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_COLLECT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_COLLECT.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_COLLECT.keys = theseKeys[-1]  # just the last key pressed
                key_COLLECT.rt = key_COLLECT.clock.getTime()
                if BARTObj.status == STARTED:
                    BARTObj.complete()
                    BARTObj.totalNumberOfPumps += BARTObj.balloonNumberOfPumps
                    BARTObj.totalPoints += BARTObj.balloonPoints
                    print('collect!')
                    port.setData(88)
                    core.wait(0.01)
                    port.setData(0)

        # *ISI* period
        if frameN >= 0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start((50-frameN)*frameDur)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period

        # *BARTObj* updates
        if frameN >= 50 and BARTObj.status == NOT_STARTED:
            # keep track of start time/frame for later
            BARTObj.tStart = t  # underestimates by a little under one frame
            BARTObj.frameNStart = frameN  # exact frame index
            BARTObj.start()
            BARTObj.makeBalloon(balloonID=thisTrial.balloonID, color=thisTrial.color, maxPumps=thisTrial.maxpumps, gainpoints=thisTrial.gainpoints, initsize=thisTrial.initsize, gainsize=thisTrial.gainsize, mon=mon)
            if frameN == 50:
                print('trial: '+str(trials.thisRepN)+'!')
                port.setData(100 + trials.thisRepN)
                core.wait(0.01)
                port.setData(0)
        if BARTObj.status == STARTED:
            if frameN >= 150:
                BARTObj.currentBaloon.pump.draw()
                BARTObj.currentBaloon.stimuli.draw()
                BARTObj.gui.draw()
                #BARTObj.fixationCross.draw()
            #else:
                #BARTObj.fixationCross.draw()
        if BARTObj.status == 'EXPLODE' and continueRoutine:
            port.setData(99)
            core.wait(0.01)
            port.setData(0)
            print('explode!')
            BARTObj.currentBaloon.explosionSound.play()
            #BARTObj.currentBaloon.stimuli.fillColor = [255, 0, 0]
            #BARTObj.currentBaloon.stimuli.lineColor = [255, 0, 0]
            BARTObj.currentBaloon.stimuli.image = "assets/bal_red.png"
            BARTObj.currentBaloon.pump.draw()
            BARTObj.currentBaloon.stimuli.draw()
            #BARTObj.fixationCross.draw()
            win.flip()
            core.wait(2)
            BARTObj.complete()
        if BARTObj.status == FINISHED and continueRoutine:
            key_PUMP.status = FINISHED
            key_COLLECT.status = FINISHED
            continueRoutine = False
            BARTObj.gui.update(BARTObj.balloonPoints,BARTObj.totalPoints)
            BARTObj.showSummary()
            win.flip()
            core.wait(4)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_PUMP.keys in ['', [], None]:  # No response was made
        key_PUMP.keys = None
    # store data for trials (TrialHandler)
    trials.addData('key_PUMP.keys', key_PUMP.keys)
    if key_PUMP.keys != None:  # we had a response
        trials.addData('key_PUMP.rt', key_PUMP.rt)

    # check responses
    if key_COLLECT.keys in ['', [], None]:  # No response was made
        key_COLLECT.keys = None
    # store data for trials (TrialHandler)
    trials.addData('key_COLLECT.keys', key_COLLECT.keys)
    if key_COLLECT.keys != None:  # we had a response
        trials.addData('key_COLLECT.rt', key_COLLECT.rt)

    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 5 repeats of 'trials'
print('the end!')
port.setData(11)
core.wait(0.01)
port.setData(0)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
