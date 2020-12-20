from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def sounds():
	return render_template("MainPage.html")

@app.route("/journal")
def writing():
	return "Love Music ALOT"

if __name__ == "__main__":
	app.run(debug=True)