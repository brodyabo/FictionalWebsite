from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/index')
def products():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/confirmation')
def confirmation():
   name = request.args.get("username")
   email = request.args.get("email")
   props + {
       "name": name,
       "email": email
   }
   print(name)
    return render_template("confirmation.html")

if __name__ == '__main__':
    app.run(debug=True)


