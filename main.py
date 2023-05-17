from flask import Flask, render_template, request
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
    return render_template('index.html')


# Обработка данных из формы
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(username,email,password)
        if not len(username) < 20:
            error_username = 'Invalid username'
        else:
            error_username = ''
        if not 8<len(password):
            error_password = 'Invalid password'
        else:
            error_password = ''
        if error_username or error_password:
            return render_template('reg.html', error_username=error_username, error_password=error_password, username=username, email=email)
        else:
            return render_template('index.html')
    else:
        return render_template('reg.html', error_username='', error_email='',error_password='', username='', email='')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username_or_email']
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
            return render_template('index.html')
    else:
        return render_template('log.html', error_username='',error_password='', username='')


if __name__ == '__main__':
    # db_session.global_init("db/our_social_web.db")
    app.run(port=8080, host='127.0.0.1')
