from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# import mp
import threading
import os

# ---------------------------------------------------------------
import pyglet     # import pyglet
import datetime   
import os
import time
import threading
# import pyglet.media as media
import cv2
import numpy as np

# ---------------------------------------------------------------


app = Flask(__name__)
socketio = SocketIO(app)

mplayer=None
values = {
    'slider1': 0,
    'slider2': 100,
}
play_pause=False
next_dur=0
@app.route('/')
def index():
    print("new index")
    return render_template('index.html',**values)

@socketio.on('connect')
def test_connect():
    print("new connection")

    global mplayer
    global player
    player=None
    mplayer=threading.Thread(target=player_thread,args=())
    mplayer.daemon=True
    mplayer.start()


    files = os.listdir("songs")
    # print(files)
    emit('after connect',  {'data':'Lets dance','list':files})
    # emit('after connect',  {'data':'Lets dance','list':files})
@socketio.on('Slider value changed')
def value_changed(message):
    print(message)
    values[message['who']] = message['data']
    print("value changed")
    emit('update value', message, broadcast=True)
    # print(int(message['data']))
    if message['who']=='slider1':
        seek(int(message['data']))
    else:
        volume(int(message['data']))    

@socketio.on('play_pause')
def button_pressed(message):
    # values[message['who']] = message['data']
    # emit('update value', message, broadcast=True)
    global play_pause
    global player
    # emit('after connect',  {'data':'play'})
    print("play/pause")    
    if play_pause:
        print('pause')
        pause()
    else:
        play()
        print('playing')
    play_pause = not play_pause
    # emit('update value', {
    #     "who" :'slider1',
    #     "data":str(int(player.time))
    #     })
    # emit('after connect',  {'data':'play'})

@socketio.on('play track')
def play_track(msg):
    print("songs\\"+msg['data'])
    global player
    global next_dur

    # player = pyglet.media.Player()
    song = pyglet.media.load(str("songs\\"+msg['data']), streaming=False)
    # next_dur=song.duration
    # print(next_dur)
    player.queue(song)
    
    # player.next_source()
@socketio.on('next')
def next(msg):
    print('next')
    global player
    nextsong()
    next_dur=player.source.duration
    print(next_dur)
    emit('set max',{'length':next_dur})




def value_updated(value):
    # emit('update value', {
    #     "who" :'slider1',
    #     "data":str(value)
    #     })
    emit('after connect',  {'data':str(value)})
# ---------------------------------------------------------------

flag = False
exit_flag=False
player=None
# nextflag=False
def player_thread():
    global player
    # global nextflag
    files = os.listdir("songs")
    print(files[0])
    music = pyglet.resource.media(str("songs\\"+files[0]), streaming=False)
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
        # if player.playing and player.time>1:
        #     print(player.time)
        #     value_updated(int(player.time))
        
    pyglet.clock.schedule_interval(update, 0.1) 
    pyglet.app.run()
def seek(value):
    global player
    player.seek(value)  
def play():
    global flag
    flag = True    
def pause():
    global flag
    flag = False
def exit():
    global exit_flag
    exit_flag = True
def nextsong():
    global player
    player.next_source()
def volume(value):
    global player
    player.volume= value/100  
# ---------------------------------------------------------------
 

# mplayer=threading.Thread(target=player_thread,args=())
# mplayer.daemon=True
# mplayer.start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')