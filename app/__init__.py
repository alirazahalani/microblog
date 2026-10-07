from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret_key_ali"


from app import routes

