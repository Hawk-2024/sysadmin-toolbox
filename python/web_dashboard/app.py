from flask import Flask, render_template
import shutil, os

app = Flask(__name__)

@app.route("/")
def index():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return render_template("index.html", usage=percent_used)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
