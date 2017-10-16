from flask import Flask
import os, sys

# the next lines help to identify the projects root as root_path 
root_path = os.path.abspath(os.path.dirname(__file__))
root_path = root_path.split(sep='/')
root_path.pop()
root_path = '/'.join(root_path)

# project modules from /services
sys.path.append(str(root_path) + '/services')
import handshake_message

#from handshake_message import handshake_message

app = Flask(__name__)

@app.route('/')
def handshaker():
    return handshake_message.modelPredict()


if __name__=='__main__':
    app.run(debug=True)
