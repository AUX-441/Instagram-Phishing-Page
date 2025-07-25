Flask Educational Login Page  Credential Capture Simulation
 Legal Disclaimer
 This project is strictly for educational and ethical testing purposes only.
 It is intended to help developers, penetration testers, and security researchers understand how
 phishing works so they can protect users from real-world attacks.
 Any unauthorized, malicious, or illegal use of this project is strictly prohibited.
 The author is not responsible for any misuse or damage caused by this tool.
 About This Project
 This is a simple Flask-based web application that simulates a fake login page.
 It accepts user credentials (username and password) and writes them to a local file (credentials.txt).
 The primary goal is to raise awareness about phishing risks and help improve defensive strategies
 through ethical demonstrations.
 Educational Use Cases- Security awareness training- Ethical hacking demonstrations- Capture-the-flag (CTF) exercises- Simulated phishing tests in controlled environments
 Project Structure
project/
 static/                 # Static assets (css, js, images)
    css/
    js/
    images/
 templates/
    index.html          # Fake login page UI
 app.py                  # Flask backend logic
 credentials.txt         # Captured login data
 requirements.txt        # Python dependencies
 README.md               # Project documentation
 How to Run
 1. Clone the Repository
 git clone https://github.com/your-username/educational-login-sim.git
 cd educational-login-sim
 2. Set Up a Virtual Environment (Recommended)
 python -m venv venv
 source venv/bin/activate  # Windows: venv\Scripts\activate
 3. Install Dependencies
 pip install -r requirements.txt
4. Start the Flask Server
 python app.py
 Then open your browser and visit:
 http://127.0.0.1:5000
 Technologies Used- Python 3- Flask Web Framework- HTML, CSS, JavaScript- JSON APIs- Local text file logging
 What Happens on Login?- Credentials are sent via JavaScript to the /login route- Flask receives the POST request- Credentials are saved in credentials.txt- A fake error message is shown to simulate login failure
 Example saved data:
 testuser:testpassword
Sample JavaScript (Frontend)
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
 Ethical Guidelines- Always get written permission if testing with real users- Do not deploy on public or production environments- Make it clear that the page is part of a simulation- Delete captured data after training/demo
 License
 This project is licensed under the MIT License.
Author
 Educational Project by [YourName]
 Security Awareness & Ethical Hacking Trainer
 Stay secure. Stay informed
