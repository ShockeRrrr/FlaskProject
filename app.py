from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.Text, nullable=False)
    message = db.Column(db.Text, primary_key=True)

    def __repr__(self):
        return '<Article %r>' % self.id





@app.route('/')
def index():
    return render_template('header-bottom.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html')
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
