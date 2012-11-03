import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('master.html')

if __name__ == "__main__":
    host = 'IP' in os.environ and os.environ['IP'] or '0.0.0.0';
    port = 'PORT' in os.environ and int(os.environ['PORT']) or 7000;
    app.run(host=host, port=port)
