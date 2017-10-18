from flask import Flask, redirect, url_for
import os, sys

# the next lines help to identify the projects root as root_path 
root_path = os.path.abspath(os.path.dirname(__file__))
root_path = root_path.split(sep='/')
root_path.pop()
root_path = '/'.join(root_path)

# project modules from /services
sys.path.append(str(root_path) + '/services')
import handshake

app = Flask(__name__)

@app.route('/service_unknown')
def tell_the_404():
    return b'you invoked a non-existing service'

@app.route('/services/handshake')
def do_the_handshake():
    handshake.modelRequire()
    return handshake.modelPredict(handshake.modelTransform('{}'))

@app.route('/models/<model>')
def do_redirect(model):
    if model == 'handshake':
        return redirect(url_for('do_the_handshake'), code=301)
    else:
        return redirect(url_for('tell_the_404'), code=404)

if __name__=='__main__':
    app.run(debug=True)

