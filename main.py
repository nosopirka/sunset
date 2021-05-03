from flask import Flask, render_template, request, make_response, session, redirect, abort
from data import db_session
import sqlite3
from flask import make_response, jsonify
from data.linked import Linked

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'


def main():
    db_session.global_init("db/link.db")
    app.run()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db_sess = db_session.create_session()
        text = request.form['text']
        db_sess.add(Linked(text=text))
        db_sess.commit()
        return redirect('/')
    return render_template("base.html", title="Главная", form=Linked)


@app.route("/link")
def link():
    con = sqlite3.connect("db/link.db")
    cur = con.cursor()
    links = cur.execute("""SELECT text FROM links""").fetchall()
    con.close()
    return render_template("link.html", title="Ссылки", content=links)


if __name__ == '__main__':
    main()