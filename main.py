from  flask import  Flask,render_template,flash,redirect,url_for,request
import pymysql
from datetime import datetime



db_config={

    "host":"sql10.freesqldatabase.com",
    "user":"sql10742241",
    "password":"UtlxCngsn8",
    "database":"sql10742241"
}


app = Flask(__name__)

app.secret_key="brightonbeatliverpoll"

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/navbar")
def navbar():
   return render_template("navbar.html")

@app.route("/procedures")
def procedures ():
   return render_template("procedures.html")


@app.route("/add_members" , methods=(["GET","POST"]))
def add_members():

    if request.method == "POST":

   # Get data from the form
        identity = request.form.get('identity')
        member_nidc = request.form.get('member_nidc')
        member_location = request.form.get('member_location')
        member_phone = request.form.get('member_phone')
        ticket_number = request.form.get('ticket_number')
        time_arrived = datetime.now()  # Automatically get the current time
        # Connect to the database and insert the new member
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO `invites` (`identity`, `member_nidc`, `member_location`, 
                `member_phone`, `time_arrived`, `ticket_number`) 
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (identity, member_nidc, member_location, member_phone, time_arrived, ticket_number))
                connection.commit()  # Commit the transaction
                flash("you joined our group")
                
        finally:
            connection.close()  # Ensure the connection is closed

        return redirect(url_for('Home'))  # Redirect to the same page or another page after submission
   
    return render_template("join.html")  # Render the form for GET requests




if __name__ == "__main__":
  app.run(debug=False , host="0.0.0.0")
