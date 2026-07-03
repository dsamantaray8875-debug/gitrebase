from flask import Flask
import os windows

app = Flask(__name__)

@app.route("/differentline")
def hello():
    return "updated Flask sample application on azure hghapp service updated version-6"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7000))  #7000  9000
    app.run(host="0.0.0.0", port=port, debug=False)

