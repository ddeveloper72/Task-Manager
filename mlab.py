from flask import Flask

app = Flask(__name__)

def auth():
    app.config["MONGO_URI"] = 'mongodb://root:dandn72@ds155352.mlab.com:55352/task_manager'
    return auth