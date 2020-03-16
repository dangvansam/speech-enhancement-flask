import os
import requests
from flask import Flask, escape, request, render_template, session
from src.add_noise import add_noise_one
from src.prediction_denoise import predictOne
import random
app = Flask(__name__)

@app.route('/')
def home():    
    if 'filename' in session:
        #os.remove('static/uploaded/' + session['filename'])
        session.pop('filename')
    if 'noise_filename' in session:
        #os.remove('static/uploaded/' + session['noise_filename'])
        session.pop('noise_filename')
    if 'denoise_filename' in session:
        #os.remove('static/uploaded/' + session['denoise_filename'])
        session.pop('denoise_filename')
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def uploadFile():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        print(filename)
        file.save('static/uploaded/'+filename)
        session['filename'] = filename
        if 'noise_filename' in session:
            #os.remove('static/uploaded/' + session['noise_filename'])
            session.pop('noise_filename')
        return render_template('index.html', filename=filename)

@app.route('/addnoise<string:id>')
def addNoise(id):
    if 'filename' not in session:
        return home()
    if os.path.exists('static/uploaded/' + 'denoise_' + session['filename']):
        os.remove('static/uploaded/' + 'denoise_' + session['filename'])
    if 'noise_filename' in session:
        os.remove('static/uploaded/' + session['noise_filename'])
        session.pop('noise_filename')
    #if 'noise_filename' not in session:
    noise_file = random.choice(os.listdir('data/noise/' + id))
    print('noise_file:',id,noise_file)
    add_noise_one('static/uploaded/' + session['filename'], 'data/noise/{}/{}'.format(id,noise_file),'static/uploaded/noise_' + id + session['filename'])
    session['noise_filename'] = 'noise_' + id + session['filename']
    return render_template('index.html', filename=session['filename'], noise_filename=session['noise_filename'])


@app.route('/denoise')
def removeNoise():
    if 'filename' not in session:
        return home()
    if 'noise_filename' not in session:
        return home()
    predictOne('static/uploaded/' + session['noise_filename'], 'static/uploaded/denoise_' + session['filename'])
    session['denoise_filename'] = 'denoise_' + session['filename']
    #session.pop('noise_filename')
    return render_template('index.html', filename=session['filename'], noise_filename=session['noise_filename'], denoise_filename=session['denoise_filename'])

if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'dangvansam'
    app.run()