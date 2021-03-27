from flask import Flask, render_template, request

from models import word_corr, detect_text, API
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'Corp_website'


@app.route("/")
def hello():
    return render_template('index.html', name='')


#@app.route("/proj1")
#def upload_file():
#    results={}
#    return render_template('proj1.html', value=results)


@app.route("/proj1",methods=["GET", 'POST'])
def Proj1():
    results={}
    if request.method == 'POST':
        f = request.files['file']

        f.save(secure_filename(f.filename))
        print(f.filename)
        results['text'] = detect_text(f.filename, API)
        print(results)
    return render_template('proj1.html', value=results)


@app.route("/proj2", methods=["GET", 'POST'])
def proj2():
    content = {}
    option = ''
    if request.method == 'POST':
        f = request.form['sample']

        word,options = word_corr(f)
        content['words'] = word
        option = options
        print(options)
        print(content)
        # do logic here
    return render_template('proj2.html', value=content, value2=option)




@app.route("/styles")
def styles():
    return render_template('styles.html')


@app.route("/base")
def base():
    return render_template('base.html')






if __name__ == "__main__":
    app.run(debug=True)
