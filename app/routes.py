from app import app


@app.route('/')
@app.route('/home/')
def hello():
    return 'Hello World!'


@app.route('/about')
def about():
    return "About Microblog"
