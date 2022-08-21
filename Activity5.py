from flask import Flask
import time
import os


app = Flask(__name__)


@app.route('/')
def get_coordinates():
    return str(time.time())


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6738))
    app.run(host='0.0.0.0', port=port)
