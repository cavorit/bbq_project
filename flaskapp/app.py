from flask import Flask
from handshake_message import handshake_message


app = Flask(__name__)

@app.route('/')
@app.route('/handshake')
def handshake():
    return handshake_message()

if __name__ == '__main__':
    app.run(debug=True)
