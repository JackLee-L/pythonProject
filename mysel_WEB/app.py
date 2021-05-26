from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('myself_index.html')

# @app.route('/')
# def myself_index_bak():
#     return render_template('myself_index_bak.html')


if __name__ == '__main__':
    # app.debug = True
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
