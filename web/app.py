import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Le Flask running on %s:%s" % ( os.environ['IP'], os.environ['PORT'])

if __name__ == "__main__":
    app.run(host=os.environ['IP'], port=os.environ['PORT'])
    