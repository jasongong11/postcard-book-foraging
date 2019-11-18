#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Oct 17 22:59:59 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/gongxuanjun/OneDrive - University of California, Davis/Projects/Information Foraging and multitasking/measure/information_foraging_novelty_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to our experiment!\n\nPress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
Picture1 = visual.ImageStim(
    win=win,
    name='Picture1', 
    image='pictures/1.jpg', mask=None,
    ori=0, pos=(0.3, 0.3), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Picture2 = visual.ImageStim(
    win=win,
    name='Picture2', 
    image='pictures/2.jpg', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Picture3 = visual.ImageStim(
    win=win,
    name='Picture3', 
    image='pictures/3.jpg', mask=None,
    ori=0, pos=(-0.3, 0.3), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Picture4 = visual.ImageStim(
    win=win,
    name='Picture4', 
    image='pictures/4.jpg', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()
picture_list = list(range(1, 51))
novel_list = list(range(1, 51))
non_novel_list = []
n = [0, 1, 2, 3, 4]
p_rich = [0.35, 0.35, 0.1, 0.1, 0.1]
p_scarce = [0.1, 0.1, 0.1, 0.35, 0.35]

# test

chosen_novel = np.random.choice(novel_list, 4, replace=False)
np.random.shuffle(chosen_novel)

showing = chosen_novel
showing_1 = showing[0]
showing_2 = showing[1]
showing_3 = showing[2]
showing_4 = showing[3]

non_novel_list = np.concatenate((non_novel_list, chosen_novel))
novel_list = [x for x in novel_list if x not in chosen_novel]




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
# update component parameters for each repeat
welcome_key_resp.keys = []
welcome_key_resp.rt = []
# keep track of which components have finished
welcomeComponents = [text, welcome_key_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *welcome_key_resp* updates
    waitOnFlip = False
    if welcome_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_key_resp.frameNStart = frameN  # exact frame index
        welcome_key_resp.tStart = t  # local t and not account for scr refresh
        welcome_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_key_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            welcome_key_resp.keys = theseKeys.name  # just the last key pressed
            welcome_key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if welcome_key_resp.keys in ['', [], None]:  # No response was made
    welcome_key_resp.keys = None
thisExp.addData('welcome_key_resp.keys',welcome_key_resp.keys)
if welcome_key_resp.keys != None:  # we had a response
    thisExp.addData('welcome_key_resp.rt', welcome_key_resp.rt)
thisExp.addData('welcome_key_resp.started', welcome_key_resp.tStartRefresh)
thisExp.addData('welcome_key_resp.stopped', welcome_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    n_novel = int(np.random.choice(n, 1, p_rich))
    n_non_novel = 4 - n_novel
    
    chosen_novel = np.random.choice(novel_list, n_novel, replace=False)
    chosen_non_novel = np.random.choice(non_novel_list, n_non_novel, replace=False)
    
    chosen_novel = list(chosen_novel)
    chosen_non_novel = list(chosen_non_novel)
    np.random.shuffle(chosen_novel)
    np.random.shuffle(chosen_non_novel)
    
    print(chosen_novel, chosen_non_novel)
    showing = np.concatenate((chosen_novel, chosen_non_novel))
    
    showing_1 = showing[0]
    showing_2 = showing[1]
    showing_3 = showing[2]
    showing_4 = showing[3]
    
    
    # keep track of which components have finished
    trialComponents = [Picture1, Picture2, Picture3, Picture4, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Picture1* updates
        if Picture1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Picture1.frameNStart = frameN  # exact frame index
            Picture1.tStart = t  # local t and not account for scr refresh
            Picture1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Picture1, 'tStartRefresh')  # time at next scr refresh
            Picture1.setAutoDraw(True)
        
        # *Picture2* updates
        if Picture2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Picture2.frameNStart = frameN  # exact frame index
            Picture2.tStart = t  # local t and not account for scr refresh
            Picture2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Picture2, 'tStartRefresh')  # time at next scr refresh
            Picture2.setAutoDraw(True)
        
        # *Picture3* updates
        if Picture3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Picture3.frameNStart = frameN  # exact frame index
            Picture3.tStart = t  # local t and not account for scr refresh
            Picture3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Picture3, 'tStartRefresh')  # time at next scr refresh
            Picture3.setAutoDraw(True)
        
        # *Picture4* updates
        if Picture4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Picture4.frameNStart = frameN  # exact frame index
            Picture4.tStart = t  # local t and not account for scr refresh
            Picture4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Picture4, 'tStartRefresh')  # time at next scr refresh
            Picture4.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Picture1.started', Picture1.tStartRefresh)
    trials.addData('Picture1.stopped', Picture1.tStopRefresh)
    trials.addData('Picture2.started', Picture2.tStartRefresh)
    trials.addData('Picture2.stopped', Picture2.tStopRefresh)
    trials.addData('Picture3.started', Picture3.tStartRefresh)
    trials.addData('Picture3.stopped', Picture3.tStopRefresh)
    trials.addData('Picture4.started', Picture4.tStartRefresh)
    trials.addData('Picture4.stopped', Picture4.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    non_novel_list = np.concatenate((non_novel_list, chosen_novel))
    novel_list = [x for x in novel_list if x not in chosen_novel]
    
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
