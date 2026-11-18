
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Training</title>
        </head>
        <body>
            <h1>Welcome To DevOps</h1>
            <h2>CI/CD Pipeline Successfully Deployed!</h2>
            <p>Version: 2.0</p>
            <p>Deployed automatically using GitHub Actions.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
