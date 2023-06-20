# from flask import Flask

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return "<p>Hello World!</p>"

# if __name__ == '__main__': 
#     app.run(debug=True)


from flask import Flask
app = Flask(__name__)

app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True, port=5001)
