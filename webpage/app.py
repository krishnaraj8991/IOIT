# from flask import Flask
from flask import Flask, render_template, request
from werkzeug import secure_filename
# import threading


   
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
