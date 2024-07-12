#imports
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#define the sql uri
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbs.db'

#define database
db = SQLAlchemy(app)

#define the user model and iput all the columns we need
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(58), nullable=False)
    author = db.Column(db.String(58), nullable=False)
    publication = db.Column(db.String(58), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()

    #created the routes books, add-book, new book
@app.route('/')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication']

        new_book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template('add_books.html', title='Add a book')

if __name__ == '__main__':
    create_db()
    app.run(port=8080, debug=True)

    