from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/results',methods=['POST'])
def results_page():
    return render_template("index.html")
