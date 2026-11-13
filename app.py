from flask import Flask, render_template, request
from models import Resume
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/buildresume_Name', methods=['POST'])
def build_resume():
    return render_template("buildresume_Name.html")
    pass

@app.route('/loadresume', methods=['POST'])
def load_resume():
    return render_template("loadresume.html")
    pass

@app.route('/name', methods=['POST'])
def get_name():
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    global fullname
    fullname = f"{firstname} {lastname}"
    return render_template("buildresume_Title.html")

@app.route('/title', methods=['POST'])
def get_title():
    global title
    title = request.form['title']
    return render_template("buildresume_Work_Experience.html")

@app.route('/work_experience', methods=['POST'])
def get_work_experience():
    pass

if __name__ == '__main__':
    app.run(debug=True)
