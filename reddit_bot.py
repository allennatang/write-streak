import praw
import config
from flask import session


#Login to Reddit
def bot_login(my_username, my_password):
    reddit = praw.Reddit(
        username=my_username,
        password=my_password,
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent="bbrioche12's dog comment responder bot v0.1"
    )
    return reddit
    
def run_bot(reddit):
    for comment in reddit.comments:
        if 'dog' in comment.body:
            print("String found!!")

# def login_get_comments():
#     reddit = bot_login()
    
    # Create a subreddit instance
    # subreddit = reddit.subreddit('cats')
    # top_25_submissions = subreddit.hot(limit=25)
    # for submission in top_25_submissions:
    #     print(submission.title)

    # subreddit = reddit.subreddit('testingground4bots')
    # subreddit.submit(title='this is my test post', selftext='hi there')

    # submission = reddit.submission('1czdveq')
    # comments = submission.comments
    # comment_list = []
    
    # for comment in comments:
    #     if 'cat' in comment.body:
    #         #comment.reply('CAT!!!!')
    #         comment_list.append(comment.body)
    # print('done')

    # return comment_list

# app.py

from flask import Flask, request, render_template, flash, redirect
from config import Config #For logging in with Flask

app = Flask(__name__)
app.secret_key = "16248e8e662a3a95f2074c9d42f7dbbf80ad06734b1589edf2f70e1fb3aeb74c"

##Config stuff ??
app.config.from_object(Config)

#from app import routes
##

@app.route("/")

# def index():
#     if 'username' in session:
#         return f'Logged in as {session["username"]}'
#     return 'You are not logged in'

def home():
    # comment_list = login_get_comments()
    ##test_comment_list = ["omg cats", "hi cat", "my cat"]
    return render_template("base.html", 
                           title="Jinja and Flask")

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']

    username = session.get('username')
    password = session.get('password')
    reddit = bot_login(username, password)

    

    title = username
    selftext = text + username

    reddit.subreddit("testingground4bots").submit(title, selftext)

    return render_template('base.html', show_message=True, processed_text=text)

if __name__ == "__main__":
    app.run(debug=True)


import forms 
# from forms import LoginForm


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        
        session['username'] = form.username.data
        session['password'] = form.password.data

        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('base'))