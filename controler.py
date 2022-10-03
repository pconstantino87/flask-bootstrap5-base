import datetime

from flask import Flask, redirect, render_template

app = Flask(__name__, static_folder='web/assets',
            template_folder='web/templates')

year = datetime.datetime.now()
year = year.strftime("%Y")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
