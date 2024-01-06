from flask import *

### Reference through https://joachim8675309.medium.com/jenkins-ci-pipeline-with-python-8bf1a0234ec3

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def home():
    return "<h1>Welcome to Jenkins Tutorials<h1/>"

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Good Morning ! Why Hello %s!\n' % username

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
