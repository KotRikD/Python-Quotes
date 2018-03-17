from flask import Flask,render_template,session,redirect,request,url_for,Markup,jsonify
import settings
from database import *
import quotes

app = Flask(__name__)

try:
    v = settings.adm_pass
    v = settings.secret_key
except:
    print("В файле settings.py что-то отсутствует!")
    exit()

app.secret_key = settings.secret_key

@app.route("/", methods=['GET'])
def index():
    q_ = quotes.MQuo.get_random_quote()
    if request.args.get('id'):
        q_ = quotes.MQuo.get_quote(int(request.args.get('id')))

    c_ = quotes.MQuo.get_count()
    idquote = q_['id']
    textquote = Markup(q_['textqoute'])

    return render_template('index.html', textquote=textquote, idquote=idquote, c=c_)

@app.route("/addquote", methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        if 'pass' in request.form and 'text' in request.form:
            if request.form['pass'] == settings.adm_pass:
                quotes.MQuo.add_quote(request.form['text'].replace("\n", "<br>"))
    return redirect(url_for('index'))

@app.route("/api/get_random_quote")
def api_quopte():
    if not request.args.get('key') or request.args.get('key') != settings.secret_key:
        return jsonify({'error_code': 'IDI NAXUI CODE GONY PIDORAS EBLIVIJ ;3'})
    q_ = quotes.MQuo.get_random_quote()
    q_['textqoute'] = q_['textqoute'].replace("<br>", "\n")
    return jsonify(q_)

if __name__ == "__main__":
    app.run(port=5006)
