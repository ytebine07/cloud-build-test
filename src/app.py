import os
import re

from flask import Flask
import subprocess
app = Flask(__name__)


@app.route('/')
def hello_world():
    _env = os.environ.get('_ENV', 'undefined')

    orig_env = ''
    def_env = ''
    for env in os.environ:
        if re.search('^_.*$', env):
            orig_env += env + ' : ' + os.environ.get(env) + '<br>'
        else:
            def_env += env + ' : ' + os.environ.get(env) + '<br>'

    return "<h1>{}</h1><h2>自分で設定した環境変数</h2>{}<h2>デフォルト環境変数</h2>{}".format(_env, orig_env, def_env)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
