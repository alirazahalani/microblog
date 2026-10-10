import pdb
from flask import flash, render_template, redirect, url_for
from app import app, forms 


@app.route('/')
@app.route('/index/')
def home():
    user = {
        'username': "alireza"
    }
    posts = [
        {
            'author': {'username': 'alireza'},
            'body': "My First post"
        },
        {
            'author': {'username': 'yasmin'},
            'body': "My second post"
        }
    ]
    return render_template('index.html', title="Home", posts=posts, user=user)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash(f"User: {form.username.data}, logged in, {form.remember_me.data}")
        return redirect(url_for('home'))
    else:
        return render_template('login.html', form=form)