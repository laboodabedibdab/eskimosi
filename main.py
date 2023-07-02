from flask import Flask, render_template, request, make_response
import hashlib

# import db_session
# from users import User

# users = db_session.query(User).all()
#
# for user in users:
#     print(user.id, user.username, user.email)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_key'


@app.route('/')
@app.route('/index')
def index():
    if not request.cookies.get('ident'):
        return render_template('index.html')



# Обработка данных из формы
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)

        error_username = 'Invalid username' if len(username) >= 20 else ''
        error_password = 'Invalid password' if len(password) <= 8 else ''

        if error_username or error_password:
            return render_template('reg.html', error_username=error_username, error_password=error_password,
                                   username=username, password=password)
        else:
            return render_template('index.html')
    else:
        return render_template('reg.html', error_username='', error_password='', username='', password='')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        if not len(username) < 20:
            error_username = 'Invalid username'
        else:
            error_username = ''
        if not 8<len(password):
            error_password = 'Invalid password'
        else:
            error_password = ''
        if error_username or error_password:
            return render_template('log.html', error_username=error_username, error_password=error_password, username=username)
        else:
            res = make_response("cookie")
            res.set_cookie('ident', (lambda text: hashlib.sha256(text.encode('utf-8')).hexdigest())(), max_age=60 * 60 * 24 * 365 * 2)
            return render_template('index.html')
    else:
        return render_template('log.html', error_username='',error_password='', username='')


if __name__ == '__main__':
    # db_session.global_init("db/our_social_web.db")
    app.run(port=8080, host='127.0.0.1')
