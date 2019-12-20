import os

from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello_world():
    _env = os.environ.get('_ENV', 'undefined')
    allenv = ''
    for env in os.environ:
        allenv += env + ' : ' + os.environ.get(env) + '<br>'
    return "<h1>{}</h1>{}".format(_env, allenv)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
