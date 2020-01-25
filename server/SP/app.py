from flask import Flask, render_template,redirect,request
from flask_socketio import SocketIO, emit
# import mp
import threading
import os
import multiprocessing

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


Deviecs =["127.0.0.1","192.168.1.2","1"]
app = Flask(__name__)
socketio = SocketIO(app)
values = {
    'slider1': 0,
    'slider2': 100,
}

@app.route('/')
def index():
    user = request.args.get('user')
    if user is None:
        return render_template('index.html',**values)
    else:
        return user_login()

# @app.route('/data')
def user_login():
    user = request.args.get('user')
    global tunnels
    global rooms
    global room_id
    global person_detected
    person_detected=False
    for tunnel,idx in enumerate(tunnels):
        while not tunnel.empty():
            name=tunnel.get()
            print("names:-"+name)
            for room in rooms:
                if name in room:
                    room.remove(name)
            rooms[idx].append(name)
        print("people present in room "+idx+' are '+str(rooms[idx]))
        if user in rooms[idx]:
            print( user +' is present in room '+idx)
            room_id=idx
            person_detected=True
    
    if not person_detected:
        print( user +' is not present in any room')
    return render_template('index.html',**values)
        

@socketio.on('connect')
def test_connect():
    global Deviecs
    global person_detected
    global room_id
    if person_detected:
        emit('redirect',  {'data':str(Deviecs[room_id]+":5000")})
        
    print("new connection")
    emit('after connect',  {'data':'Connected Devices','list':Deviecs})
    # restart()
    # files = os.listdir("songs")
    # print(files)
    # emit('after connect',  {'data':'Lets dance','list':files})
# @socketio.on('Slider value changed')
# def value_changed(message):
#     print(message)
#     # values[message['who']] = message['data']
#     print("value changed")
#     emit('update value', message, broadcast=True)
#     # print(int(message['data']))
#     if message['who']=='slider1':
#         seek(int(message['data']))
#     else:
#         volume(int(message['data']))    

# @socketio.on('play_pause')
# def button_pressed(message):
#     # values[message['who']] = message['data']
#     # emit('update value', message, broadcast=True)
#     global play_pause
#     global player
#     # emit('after connect',  {'data':'play'})
#     print("play/pause")    
#     if play_pause:
#         print('pause')
#         pause()
#     else:
#         play()
#         print('playing')
#     play_pause = not play_pause
#     # emit('update value', {
#     #     "who" :'slider1',
#     #     "data":str(int(player.time))
#     #     })
#     # emit('after connect',  {'data':'play'})

# @socketio.on('play track')
# def play_track(msg):
#     print("songs\\"+msg['data'])
#     global player
#     global next_dur

#     # player = pyglet.media.Player()
#     song = pyglet.media.load(str("songs\\"+msg['data']), streaming=False)
#     # next_dur=song.duration
#     # print(next_dur)
#     player.queue(song)
    
#     # player.next_source()
# @socketio.on('next')
# def next(msg):
#     print('next')
#     global player
#     nextsong()
#     next_dur=player.source.duration
#     print(next_dur)
#     emit('set max',{'length':next_dur})




# def value_updated(value):
#     # emit('update value', {
#     #     "who" :'slider1',
#     #     "data":str(value)
#     #     })
#     emit('after connect',  {'data':str(value)})



import face_detector as fd
# detected_people=multiprocessing.Array('c',3)
if __name__ == '__main__':

    global detected_people
    global rooms
    global room_id
    global person_detected
    person_detected=False
    global tunnels
    tunnels=[]

    room_id=0


    for x in range(len(Deviecs)):
        tunnel = multiprocessing.Queue()
        tunnels.append(tunnel)

    tunnel.put("-")
    print(len(Deviecs))
    rooms=[]
    for x in range(len(Deviecs)):
        rooms.append([])
    
    rooms[1].append("-")
    # detected_people.append('-')
    # for deviec in detected_people:
    #     print("sections:-"+str(deviec))
        
    print(np.shape(rooms))
    print(rooms)
    

    # m=threading.Thread(target=fd.detector,args=(tunnel))
    # m.daemon=True
    # m.start()
    f=True
    if f:
        for idx,tunnel in enumerate(tunnels):
            p=multiprocessing.Process(target=fd.detector,args=(tunnel,str(Deviecs[idx])))
            p.start()
        socketio.run(app, host='0.0.0.0',port=2000)
    
   