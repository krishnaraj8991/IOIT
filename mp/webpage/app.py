# from flask import Flask
from flask import Flask, render_template, request
from werkzeug import secure_filename
import mp
import threading


mplayer=None
mplayer = threading.Thread(target=mp.player, args=())
mplayer.daemon=True
   
mplayer.start()
   
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/player', methods = ['GET', 'POST'])
def upload():
   mp.play()
   return render_template('upload.html')

@app.route('/response', methods = ['GET', 'POST'])
def input():
   # play/pause=request.args.get("pplay/pause")
   mp.pause()
   return render_template('upload2.html')

@app.route('/exit', methods = ['GET', 'POST'])
def input1():
   # play/pause=request.args.get("pplay/pause")
   global mplayer
   mp.pause()
   mp.exit()
   return ("thanks for comming")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
