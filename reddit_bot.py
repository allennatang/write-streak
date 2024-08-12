import praw
import config


#Login to Reddit
def bot_login():
    reddit = praw.Reddit(
        username=config.username,
        password=config.password,
        client_id=config.client_id,
        client_secret=config.client_secret,
        user_agent="bbrioche12's dog comment responder bot v0.1"
    )
    return reddit
    
def run_bot(reddit):
    for comment in reddit.comments:
        if 'dog' in comment.body:
            print("String found!!")

def login_get_comments():
    reddit = bot_login()
    
    # Create a subreddit instance
    # subreddit = reddit.subreddit('cats')
    # top_25_submissions = subreddit.hot(limit=25)
    # for submission in top_25_submissions:
    #     print(submission.title)

    # subreddit = reddit.subreddit('testingground4bots')
    # subreddit.submit(title='this is my test post', selftext='hi there')

    submission = reddit.submission('1czdveq')
    comments = submission.comments
    comment_list = []
    
    for comment in comments:
        if 'cat' in comment.body:
            #comment.reply('CAT!!!!')
            comment_list.append(comment.body)
    print('done')

    return comment_list

# app.py

from flask import Flask, request, render_template, flash, redirect
from config import Config #For logging in with Flask

app = Flask(__name__)

##Config stuff ??
app.config.from_object(Config)

#from app import routes
##


@app.route("/")

def home():
    comment_list = login_get_comments()
    ##test_comment_list = ["omg cats", "hi cat", "my cat"]
    return render_template("base.html", 
                           title="Jinja and Flask",
                           comment_list=comment_list)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    reddit = bot_login()

    title = "Streak #1"
    selftext = text

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
        return redirect('/base')
    return render_template('login.html', title='Sign In', form=form)