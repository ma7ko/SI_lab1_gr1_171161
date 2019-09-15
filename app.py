from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_BINDS'] = {'one': 'sqlite:///one.db', 'two': 'sqlite:///two.db'}
db = SQLAlchemy(app)

class PersonalInfo(db.Model):
    __bind_key__ = 'one'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    points1 = db.Column(db.Integer, default=0)
    points2 = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Person %r>' % self.id

class PersonalInfo1(db.Model):
    __bind_key__ = 'two'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    points1 = db.Column(db.Integer, default=0)
    points2 = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Person %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('proektna2.html')
@app.route('/templates/')
def algoBase2():
    return render_template('AlgoToCode.html')
@app.route('/templates1/')
def algoBase1():
    return render_template('anAlgorithm.html')
@app.route('/templates2/')
def algoBase3():
    return render_template('algo.html')
@app.route('/templates3/')
def algoBase4():
    return render_template('quizMenu.html')
@app.route('/templates4/')
def what1():
    return render_template('primeri.html')
@app.route('/templates5/')
def what2():
    return render_template('primeri2.html')
@app.route('/templates6/')
def what3():
    return render_template('primeri32.html')
@app.route('/templates7/')
def Code1():
    return render_template('toCode.html')
@app.route('/templates8/')
def Code2():
    return render_template('toCode2.html')
@app.route('/templates9/')
def Code3():
    return render_template('toCode3.html')
@app.route('/templates10/')
def some1():
    return render_template('primeri3.html')
@app.route('/templates11/')
def some2():
    return render_template('binarySearch.html')
@app.route('/templates12/', methods=['POST', 'GET'])
def quiz1():
    if request.method == 'POST':
        persons_name = request.form['name']
        persons_surname = request.form['surname']
        pointsreal = request.form['poi']
        new_person = PersonalInfo(name=persons_name, surname=persons_surname, points1=pointsreal)
        try:
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('quiz1'))
        except:
            return 'There was an issue'
    else:
        persons=PersonalInfo.query.all()
        return render_template('sort.html', persons=persons)
@app.route('/templates13/', methods=['POST','GET'])
def quiz2():
    if request.method == 'POST':
        persons_name = request.form['name']
        persons_surname = request.form['surname']
        pointsreal = request.form['poi']
        new_person = PersonalInfo1(name=persons_name, surname=persons_surname, points1=pointsreal)
        try:
            db.session.add(new_person)
            db.session.commit()
            return redirect(url_for('quiz2'))
        except:
            return 'There was an issue'
    else:
        persons=PersonalInfo1.query.all()
        return render_template('fillIn.html',persons=persons)


if __name__ == "__main__":
    app.run(debug=True)