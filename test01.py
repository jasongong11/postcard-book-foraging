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
expName = 'Media Psychological Study'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc 
#G Set data file name 
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
#G set handler(?)
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/gongxuanjun/OneDrive - University of California, Davis/Projects/Information Foraging and multitasking/measure/test01.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame


# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# *****************************
# *****************************
# *****************************

# Set up picture list for updating and randomizatin
picture_list = range(1, 401)
novel_list = range(1, 401)

selected_list = []
last_list = []

n_novel_list = [1, 2, 3, 4]

p_rich = [0.1, 0.2, 0.3, 0.4]
p_middle = [0.25, 0.25, 0.25, 0.25]
p_scarce = [0.4, 0.3, 0.2, 0.1]

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcom_text = visual.TextStim(win=win, name='text',
    text='Welcome to our experiment!\n\nPress "space" to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_key_resp = keyboard.Keyboard()

# prepare images in advance

# to delete
image = []

for i in range(1, 81):
    string = str(i) + ".jpg"
    path = os.path.join('pictures', string)
    name = "image" + str(i)
    
    temperal_image = visual.ImageStim(
    win=win,
    name=name, 
    image=path, mask=None,
    ori=0, size=(0.48, 0.48),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
    image.append(temperal_image)

# prepare cross stimuli in wait session in advance
wait_text = visual.TextStim(win=win, name='wait_text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
clock = core.Clock()
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Run welcome session
thisExp.addData('exp_session', "welcome")
welcom_continue = True
welcom_text.draw()
tThisFlip = win.getFutureFlipTime(clock=globalClock)
win.flip()
thisExp.addData('picture_start', tThisFlip)
thisExp.nextEntry()

k = ['']
welcom_count_n = 0

while welcom_continue:
    event.waitKeys(keyList = ['space'])
    
    press_time = globalClock.getTime()
    
    welcom_count_n += 1
    
    thisExp.addData('welcom_count_n', welcom_count_n)
    thisExp.addData('first_press_time', press_time)
    thisExp.nextEntry()
    
    if welcom_count_n >= 5:
        welcom_continue = False

novel_list = range(1, 79) # to delete

# start tranning session
thisExp.addData('exp_session', "trainning")
training_continue = True
n_novel = 4
training_repeat = 0
while training_continue:
    m = 4 - n_novel
    # select traning pictures from novel list and just_selected_list 
    selected_list = np.random.choice(novel_list, n_novel, replace=False)
    selected_non_novel_list = np.random.choice(last_list, m, replace=False)
    selected_list = list(selected_list)
    selected_non_novel_list = list(selected_non_novel_list)
    selected_list.extend(selected_non_novel_list)
    np.random.shuffle(selected_list)
    
    picture1 = image[selected_list[0]]
    picture2 = image[selected_list[1]]
    picture3 = image[selected_list[2]]
    picture4 = image[selected_list[3]]
    
    picture1.pos = (0.4, 0.25)
    picture2.pos = (-0.4, -0.25)
    picture3.pos = (-0.4, 0.25)
    picture4.pos = (0.4, -0.25)
    
    picture1.draw()
    picture2.draw()
    picture3.draw()
    picture4.draw()
    tThisFlip = win.getFutureFlipTime(clock = globalClock)
    win.flip()
    
    thisExp.nextEntry()
    thisExp.addData('n_novel', n_novel)
    thisExp.addData('picture_start', tThisFlip)
    thisExp.addData('pictures_selected', selected_list)
    
    # setting press n times to continue
    training_key_count_n = 0
    k_continue = True
    
    while k_continue:
        event.waitKeys(keyList = ['space'])
        
        press_time = globalClock.getTime()
        
        training_key_count_n += 1
        
        thisExp.addData('training_count_n', training_key_count_n)
        thisExp.addData('press_time', press_time)
        thisExp.nextEntry()
        
        if training_key_count_n >= 3:
            k_continue = False
    
    n_novel -= 1
    training_repeat += 1
    last_list = selected_list
    novel_list = [x for x in novel_list if x not in last_list] # remove items that has been shown before
    
    # start wait session
    wait_text.draw()
    tThisFlip = win.getFutureFlipTime(clock = globalClock)
    win.flip()
    core.wait(0.5)
    thisExp.addData('wait_onset', tThisFlip)
    
    # test if complete repeat
    if training_repeat >= 4:
        training_continue = False

# prepare test session
# creating the list of number of novel items
n_1_list = [1] * 5
n_2_list = [2] * 5
n_3_list = [3] * 5
n_4_list = [4] * 5

n_novel_list = n_1_list + n_2_list + n_3_list + n_4_list
np.random.shuffle(n_novel_list)

# start test session
thisExp.addData('exp_session', "test")
test_continue = True
test_repeat = 0
while test_continue:
    n_novel = n_novel_list[test_repeat]
    m = 4 - n_novel
    # select traning pictures from novel list and just_selected_list 
    selected_list = np.random.choice(novel_list, n_novel, replace=False)
    selected_non_novel_list = np.random.choice(last_list, m, replace=False)
    selected_list = list(selected_list)
    selected_non_novel_list = list(selected_non_novel_list)
    selected_list.extend(selected_non_novel_list)
    np.random.shuffle(selected_list)
    
    picture1 = image[selected_list[0]]
    picture2 = image[selected_list[1]]
    picture3 = image[selected_list[2]]
    picture4 = image[selected_list[3]]
    
    picture1.pos = (0.4, 0.25)
    picture2.pos = (-0.4, -0.25)
    picture3.pos = (-0.4, 0.25)
    picture4.pos = (0.4, -0.25)
    
    picture1.draw()
    picture2.draw()
    picture3.draw()
    picture4.draw()
    tThisFlip = win.getFutureFlipTime(clock = globalClock)
    win.flip()
    
    thisExp.nextEntry()
    thisExp.addData('n_novel', n_novel)
    thisExp.addData('picture_start', tThisFlip)
    thisExp.addData('pictures_selected', selected_list)
    
    # setting press n times to continue
    test_key_count_n = 0
    k_continue = True
    
    while k_continue:
        event.waitKeys(keyList = ['space'])
        
        press_time = globalClock.getTime()
        
        test_key_count_n += 1
        
        thisExp.addData('training_count_n', test_key_count_n)
        thisExp.addData('press_time', press_time)
        thisExp.nextEntry()
        
        if test_key_count_n >= 3:
            k_continue = False
    
    # start wait session
    wait_text.draw()
    tThisFlip = win.getFutureFlipTime(clock = globalClock)
    win.flip()
    core.wait(0.5)
    thisExp.addData('wait_onset', tThisFlip)
    
    test_repeat += 1
    last_list = selected_list
    novel_list = [x for x in novel_list if x not in last_list]
    
    if test_repeat >= 10:
        test_continue = False


win.close()
core.quit()




