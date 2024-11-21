from flask import Flask

app = Flask("my_app")

@app.route("/")
def home_page():
    return "<h1>Hello world</h1>"

@app.route("/about")
def about_page():
    return "<h1>This is about page...</h1>"


if __name__ == '__main__':
    app.run(debug=True)
