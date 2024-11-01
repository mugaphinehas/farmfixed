from  flask import  Flask,render_template


app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/navbar")
def navbar():
   return render_template("navbar.html")

@app.route("/procedures")
def procedures ():
   return render_template("procedures.html")



if __name__ == "__main__":
  app.run(debug=False,host="0.0.0.0")