import os

from flask import Flask, render_template
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def landing():
    return render_template('main.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    print port
    app.run(host='0.0.0.0', port=port)
