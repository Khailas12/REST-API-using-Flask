from flask import Flask, jsonify, request


app = Flask(__name__)

incomes = [
    {
        "description": "salary",
        "amount": 5000
    }
]

incomes_two = [
    {
        "description": "lottery",
        "amount": 1000.0
    }
]

@app.route("/")
def get_incomes():
    return jsonify(incomes + incomes_two)


@app.route("/incomes", methods=["POST"])
def add_incomes():
    incomes_two and incomes.append(request.get_json())
    return "", 204


if __name__ == "__main__":
    app.run(debug=True, port=5000)