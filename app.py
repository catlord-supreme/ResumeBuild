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
    company = request.form['company']
    position = request.form['position']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    description = request.form['description']
    bullets = request.form.getlist('bullets')
    global work_experience
    work_experience = {
        'company': company,
        'position': position,
        'start_date': start_date,
        'end_date': end_date,
        'description': description
    }
    return render_template("buildresume_Education.html")

@app.route('/contact_info', methods=['POST'])
def get_contact_info():
    email = request.form['email']
    city = request.form['city']
    state = request.form['state']
    linkedin = request.form['linkedin']
    phone = request.form['phone']
    global contact_info
    contact_info = {
        'email': email,
        'city': city,
        'state': state,
        'linkedin': linkedin,
        'phone': phone
    }
    return render_template("buildresume_Projects.html")

if __name__ == '__main__':
    app.run(debug=True)
