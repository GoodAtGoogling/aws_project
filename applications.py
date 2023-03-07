
from flask import Flask,request
from flask_cors import CORS
import sql_lite_db


application = Flask(__name__)
CORS(application)

@application.route("/employees")
def index():
    employees = sql_lite_db.list_employees()
    return employees

@application.route("/employees/add", methods=['GET','POST'])
def add(): 
    if request.method=="POST":
        firstName = request.form["fistName"]
        lastName = request.form["lastName"]
        emailId = request.form["emailId"]
        sql_lite_db.add_employee(firstName,lastName,emailId)

@application.route("/employee/delete/<int:id>", methods =['GET','POST'])
def delete(id):
    sql_lite_db.delete_employee(id)

@application.route("/employee/update/<int:id>", methods =['GET','POST'])
def update(id):
        if request.method=="POST":
            firstName = request.form["fistName"]
            lastName = request.form["lastName"]
            emailId = request.form["emailId"]
            sql_lite_db.update_employee(id,firstName, lastName, emailId)



if __name__=="__main__":
    sql_lite_db.create_employee_table()
    application.run()


