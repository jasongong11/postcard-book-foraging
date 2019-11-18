#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Thu Nov 14 21:23:15 2019
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
    originPath='/Users/gongxuanjun/OneDrive - University of California, Davis/projects/Information Foraging and multitasking/measure/information_foraging_novelty_task_lastrun.py',
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

# Initialize components for Routine "trainning"
trainningClock = core.Clock()
training_picture1 = visual.ImageStim(
    win=win,
    name='training_picture1', 
    image='pictures/1.jpg', mask=None,
    ori=0, pos=(0.4, 0.25), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
training_picture2 = visual.ImageStim(
    win=win,
    name='training_picture2', 
    image='pictures/2.jpg', mask=None,
    ori=0, pos=(-0.4, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
traning_picture3 = visual.ImageStim(
    win=win,
    name='traning_picture3', 
    image='pictures/3.jpg', mask=None,
    ori=0, pos=(-0.4, 0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
training_picture4 = visual.ImageStim(
    win=win,
    name='training_picture4', 
    image='pictures/4.jpg', mask=None,
    ori=0, pos=(0.4, -0.25), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
picture1 = visual.ImageStim(
    win=win,
    name='picture1', 
    image='path1', mask=None,
    ori=0, pos=(0.4, 0.25), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
picture2 = visual.ImageStim(
    win=win,
    name='picture2', 
    image='path2', mask=None,
    ori=0, pos=(-0.4, -0.25), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
picture3 = visual.ImageStim(
    win=win,
    name='picture3', 
    image='path3', mask=None,
    ori=0, pos=(-0.4, 0.25), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
picture4 = visual.ImageStim(
    win=win,
    name='picture4', 
    image='path4', mask=None,
    ori=0, pos=(0.4, -0.25), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()
picture_list = list(range(1, 51))
novel_list = list(range(1, 51))
non_novel_list = []
n = [0, 1, 2, 3, 4]
p_rich = [0.3, 0.3, 0.2, 0.1, 0.1]
p_scarce = [0.1, 0.1, 0.2, 0.3, 0.3]




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
        theseKeys = welcome_key_resp.getKeys(keyList=['space', 'a'], waitRelease=False)
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
trainings = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trainings')
thisExp.addLoop(trainings)  # add the loop to the experiment
thisTraining = trainings.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in trainings:
    currentLoop = trainings
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trainning"-------
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    # test
    
    chosen_novel = np.random.choice(novel_list, 4, replace=False)
    np.random.shuffle(chosen_novel)
    
    showing = chosen_novel
    showing_1 = int(showing[0])
    showing_2 = int(showing[1])
    showing_3 = int(showing[2])
    showing_4 = int(showing[3])
    
    path1 = os.path.joint('pictures', showing_1, '.jpg')
    path2 = os.path.joint('pictures', showing_2, '.jpg')
    path3 = os.path.joint('pictures', showing_3, '.jpg')
    path4 = os.path.joint('pictures', showing_4, '.jpg')
    # keep track of which components have finished
    trainningComponents = [training_picture1, training_picture2, traning_picture3, training_picture4, key_resp_2]
    for thisComponent in trainningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trainningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trainning"-------
    while continueRoutine:
        # get current time
        t = trainningClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trainningClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *training_picture1* updates
        if training_picture1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            training_picture1.frameNStart = frameN  # exact frame index
            training_picture1.tStart = t  # local t and not account for scr refresh
            training_picture1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(training_picture1, 'tStartRefresh')  # time at next scr refresh
            training_picture1.setAutoDraw(True)
        
        # *training_picture2* updates
        if training_picture2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            training_picture2.frameNStart = frameN  # exact frame index
            training_picture2.tStart = t  # local t and not account for scr refresh
            training_picture2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(training_picture2, 'tStartRefresh')  # time at next scr refresh
            training_picture2.setAutoDraw(True)
        
        # *traning_picture3* updates
        if traning_picture3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            traning_picture3.frameNStart = frameN  # exact frame index
            traning_picture3.tStart = t  # local t and not account for scr refresh
            traning_picture3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(traning_picture3, 'tStartRefresh')  # time at next scr refresh
            traning_picture3.setAutoDraw(True)
        
        # *training_picture4* updates
        if training_picture4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            training_picture4.frameNStart = frameN  # exact frame index
            training_picture4.tStart = t  # local t and not account for scr refresh
            training_picture4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(training_picture4, 'tStartRefresh')  # time at next scr refresh
            training_picture4.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trainning"-------
    for thisComponent in trainningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trainings.addData('training_picture1.started', training_picture1.tStartRefresh)
    trainings.addData('training_picture1.stopped', training_picture1.tStopRefresh)
    trainings.addData('training_picture2.started', training_picture2.tStartRefresh)
    trainings.addData('training_picture2.stopped', training_picture2.tStopRefresh)
    trainings.addData('traning_picture3.started', traning_picture3.tStartRefresh)
    trainings.addData('traning_picture3.stopped', traning_picture3.tStopRefresh)
    trainings.addData('training_picture4.started', training_picture4.tStartRefresh)
    trainings.addData('training_picture4.stopped', training_picture4.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trainings.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trainings.addData('key_resp_2.rt', key_resp_2.rt)
    trainings.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trainings.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    non_novel_list = np.concatenate((non_novel_list, chosen_novel))
    novel_list = [x for x in novel_list if x not in chosen_novel]
    # the Routine "trainning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trainings'


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
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
    
    showing_1 = int(showing[0])
    showing_2 = int(showing[1])
    showing_3 = int(showing[2])
    showing_4 = int(showing[3])
    
    path1 = os.path.joint('pictures', showing_1, '.jpg')
    path2 = os.path.joint('pictures', showing_2, '.jpg')
    path3 = os.path.joint('pictures', showing_3, '.jpg')
    path4 = os.path.joint('pictures', showing_4, '.jpg')
    # keep track of which components have finished
    trialComponents = [picture1, picture2, picture3, picture4, key_resp]
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
        
        # *picture1* updates
        if picture1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture1.frameNStart = frameN  # exact frame index
            picture1.tStart = t  # local t and not account for scr refresh
            picture1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture1, 'tStartRefresh')  # time at next scr refresh
            picture1.setAutoDraw(True)
        
        # *picture2* updates
        if picture2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture2.frameNStart = frameN  # exact frame index
            picture2.tStart = t  # local t and not account for scr refresh
            picture2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture2, 'tStartRefresh')  # time at next scr refresh
            picture2.setAutoDraw(True)
        
        # *picture3* updates
        if picture3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture3.frameNStart = frameN  # exact frame index
            picture3.tStart = t  # local t and not account for scr refresh
            picture3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture3, 'tStartRefresh')  # time at next scr refresh
            picture3.setAutoDraw(True)
        
        # *picture4* updates
        if picture4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture4.frameNStart = frameN  # exact frame index
            picture4.tStart = t  # local t and not account for scr refresh
            picture4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture4, 'tStartRefresh')  # time at next scr refresh
            picture4.setAutoDraw(True)
        
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
    trials.addData('picture1.started', picture1.tStartRefresh)
    trials.addData('picture1.stopped', picture1.tStopRefresh)
    trials.addData('picture2.started', picture2.tStartRefresh)
    trials.addData('picture2.stopped', picture2.tStopRefresh)
    trials.addData('picture3.started', picture3.tStartRefresh)
    trials.addData('picture3.stopped', picture3.tStopRefresh)
    trials.addData('picture4.started', picture4.tStartRefresh)
    trials.addData('picture4.stopped', picture4.tStopRefresh)
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
    
# completed 5 repeats of 'trials'


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
