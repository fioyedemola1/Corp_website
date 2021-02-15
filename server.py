from flask import Flask, render_template

app = Flask(__name__)

#
# @app.route("/")
# def hello():
#     return render_template('index.html', name='')


@app.route("test")
def test():
    return 'here i am'







if __name__ == "__main__":
    app.run(debug=True)
