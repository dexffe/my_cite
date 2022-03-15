from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return '''<html>
            Ольга Николаевна, вы лучшая!
            </html>
            '''


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=5000)
