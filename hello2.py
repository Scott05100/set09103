from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def root():
    return render_template('hello.html')


@app.route("/AboutTheTutors/")
def AboutTheTutors():
    return render_template('AboutTheTutors.html')
    
@app.route("/Account/")
def Account():
    return render_template('Account.html')

@app.route("/AboutTheSubjects/")
def AboutTheSubjects():
    return render_template('AboutTheSubjects.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

