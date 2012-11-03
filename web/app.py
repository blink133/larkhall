import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('master.html')

if __name__ == "__main__":
    app.run(host=os.environ['IP'], port=os.environ['PORT'])
    