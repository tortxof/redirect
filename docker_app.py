import os
from urllib.parse import urlencode

from flask import Flask, request, redirect

app = Flask(__name__)

app.config['LAMBDA_APP_URL'] = os.environ.get('LAMBDA_APP_URL')

@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    return redirect(
        app.config['LAMBDA_APP_URL']
        + '?'
        + urlencode({
            'domain': request.host,
        })
    )

if __name__ == '__main__':
    app.run('0.0.0.0')
