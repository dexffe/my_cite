from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return '''<html>
            Я это сделал УРАААААААА!
            </html>
            '''


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=5000)
    print(app.run(host='0.0.0.0', port=5000))
