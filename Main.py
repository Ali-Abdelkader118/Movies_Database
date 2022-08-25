from flask import Flask , render_template
import openpyxl
# import selenium

movies_app = Flask(__name__)

@movies_app.route("/")
def homepage():
    return render_template("Home.html" , title = "Netflix")


if __name__ == "__main__" :
    movies_app.run(debug = True , port = 9000)