from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', name='')


@app.route("/proj1",methods=["GET", 'POST'])
def Proj1():
    f = request.files['file'].read()
    # do logic here
    return render_template('proj1.html')



@app.route("/proj2", methods=["GET", 'POST'])
def proj2():
    value = {'thing': 'thank you', 'okay': 'lols'}
    if request.method == 'POST':
        f = request.files['file'].read()
        # do logic here
    return render_template('proj2.html',value=value)




@app.route("/styles")
def styles():
    return render_template('styles.html')






if __name__ == "__main__":
    app.run(debug=True)
