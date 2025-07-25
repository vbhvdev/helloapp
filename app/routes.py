from flask import redirect, url_for, render_template, request, flash
from app import app, db
from app.forms import UserForm
from app.models import User

user_data = {
        'John': {'age': 28, 'email': 'john@example.com'},
        'Rose': {'age': 25, 'email': 'rose@example.com'},
        'Vaibhav': {'age': 27, 'email': 'vaibhav@example.com'},
        'Manan': {'age': 27, 'email': 'manan@example.com'},
        'Kinshu': {'age': 26, 'email': 'kinshu@example.com'}
    }


@app.route('/')
# def hello():
#     return "Hello World!!!"
def hello():
    return render_template('index.html', page_name = 'Home')


@app.route('/user/<username>')
# def hello_user(username):
#     return f'Hello {username}!!!'
def hello_user(username):
    user_dtls = user_data.get(username, {'age': 'Unknown', 'email': 'Not available'})
    return render_template('index.html', page_name ='User', user=username, age = user_dtls['age'], email = user_dtls['email'])


@app.route('/users/')
def display_users():
    return render_template('users.html', page_name ='Users', users=user_data.keys())


@app.route('/user/<username>/<int:age>')
def display_age(username, age):
    return f'Hello {username}!!!<br> You are {age} years old'

@app.route('/greet/user/<uname>')
def greet_user(uname):
    return redirect(url_for('hello_user', username=uname))

@app.route('/adduser', methods = ['GET', 'POST'])
def useradd():
    form = UserForm()
    if request.method == 'POST':
        user = User(username=form.username.data, age=form.age.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'{form.username.data} User added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding user: {str(e)}', 'danger')
        return redirect(url_for('hello'))
        
    return render_template('adduser.html', form = form)

# print(app.url_map)
