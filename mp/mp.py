import pyglet     # import pyglet
import datetime   
import os
import time
import threading
# import pyglet.media as media
import cv2
import numpy as np


def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,200,nothing)
cv2.createTrackbar('seek','image',0,210,nothing)

# cv2.createTrackbar('G','image',0,8,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON\n'
cv2.createTrackbar(switch, 'image',0,1,nothing)

switch1 = '0 : play \n1 : pause\n'
cv2.createTrackbar(switch1, 'image',0,1,nothing)


font=[cv2.FONT_HERSHEY_COMPLEX
,cv2.FONT_HERSHEY_COMPLEX_SMALL
,cv2.FONT_HERSHEY_DUPLEX
,cv2.FONT_HERSHEY_PLAIN
,cv2.FONT_HERSHEY_SCRIPT_COMPLEX
,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
,cv2.FONT_HERSHEY_SIMPLEX
,cv2.FONT_HERSHEY_TRIPLEX
,cv2.FONT_ITALIC]


# # pass sound file path 
music = pyglet.resource.media('Whatever_It_Takes2.wav')
# # play sound
# music.play()
# # keep pyglet function alive
player = pyglet.media.Player()
player.queue(music)
player.play()
flag = False
pre_r =0
def update(dt):
    # print(player.time)
    
    global flag
    global pre_r
    cv2.imshow('image',img)
    cv2.waitKey(1) & 0xFF
    r =  cv2.getTrackbarPos('seek','image')
    if r != pre_r:
        flag = True
        pre_r=r
    cv2.setTrackbarPos("R","image",int(player.time))
    s = cv2.getTrackbarPos(switch,'image')
    s1 = cv2.getTrackbarPos(switch1,'image')
    if s1==1:
        player.pause()
    else :
        if not player.playing:
            player.play()
    if s == 1:
        pyglet.app.exit()            
    else:
        img[:] = [255,255,255]
        cv2.putText(img,str(datetime.timedelta(seconds = int(player.time))), (58,177), font[2], 2, 255)
    if flag:    
        player.seek(r)
        flag = False
    




pyglet.clock.schedule_interval(update, 0.1)        
pyglet.app.run()
# pyglet.app.exit()
cv2.destroyAllWindows()
