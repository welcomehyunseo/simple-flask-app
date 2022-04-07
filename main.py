from flask import Flask, jsonify
from flask.templating import render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/click_print_button", methods=["POST"])
def click_print_button():
    print("Click print button.")
    return jsonify({"success": True})


@app.route("/get_users", methods=["GET"])
def get_users():
    from faker import Faker
    fake = Faker()
    data = []

    for i in range(0, 1000):
        data.append(fake.simple_profile())
        
    return jsonify({
        "success": True,
        "data": data
    })


app.run()
