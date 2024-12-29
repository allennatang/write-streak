import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'password123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')


username = 'bbrioche12'
password = "mCiSl1k3:'"
client_id = 'CgETnW-X8DU8eCAvgzCJ1g'
client_secret = 'GFoMEn2R-HdPaxX-7PiCmzPBoiel-Q'