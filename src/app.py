import os

from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello_world():
    target = os.environ.get('TARGET', 'World')
    env = os.environ.get('_ENV', 'DEFAULT')
    containerId = os.environ.get('HOSTNAME', 'XXXXXXX')
    allenv = ''
    for env in os.environ:
        allenv += env + ' : ' + os.environ.get(env) + '<br>'

    hostname = subprocess.check_output('hostname')
    return hostname
    # return "Hello {}!<br>Here is {}<br>ContainerID is {} <br>all : ".format(target, env, containerId)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
