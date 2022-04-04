from crypt import methods
from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# http://localhost:5000/home
@app.route("/home")
def hello_world():
    return render_template('index.html')


@app.route("/click_print_button", methods=["POST"])
def click_print_button():
    print("Click print button.")
    return jsonify({"success": True})


app.run()
