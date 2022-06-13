from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])

def index():
    return "starting machine learning project"


if __name__ == "__main__":
    app.run(debug = True)

# heroku api key - df950c89-2375-4ba3-a37b-0d8e53deb41f
# heroku app name - fsds-ml-regression
# heroku email - manimanideep345@gmail.com


