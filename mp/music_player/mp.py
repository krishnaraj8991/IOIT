import pyglet     # import pyglet
import datetime   
import os
import time
import threading
# import pyglet.media as media
import cv2
import numpy as np

flag = False
exit_flag=False
player=None
def player_thread():
    global player
    music = pyglet.resource.media('Whatever_It_Takes2.wav')
    player = pyglet.media.Player()
    player.queue(music)
    def update(dt):
        if flag:
            if not player.playing:
                player.play()
        else:
            if player.playing:
                player.pause()
        if exit_flag:
            pyglet.app.exit()
        
    pyglet.clock.schedule_interval(update, 0.1) 
    pyglet.app.run()
    
def play():
    global flag
    flag = True    
def pause():
    global flag
    flag = False
def exit():
    global exit_flag
    exit_flag = True
