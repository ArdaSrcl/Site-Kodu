from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name") #name i ceker
    processed_name = name.upper() 
    return f"Processed Name: {processed_name}"

@app.route("/members/")
def members():
    return render_template("members.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)