from written_english.convert import convert
from flask import *

obj = convert()
app = Flask(__name__)


@app.route('/<text>', methods=['GET'])
def do_task(text):
    return obj.convert_(text)


if __name__ == '__main__':
    app.run(debug=True)
