from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def process():
    if request.method == "POST":
        name = request.form.get("name")
        processed_name = name.upper()

        # Alınan ismi bir dosyaya yazma
        with open("kayitlar.txt", "a") as file:
            file.write(processed_name + "\n")

        return redirect(url_for('home', success=True))
    else:
        return "HTTP method not allowed"

@app.route("/members/")
def members():
    return render_template("members.html")

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
