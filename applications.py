
import requests
import sql_lite_db
from flask import Flask
from flask_cors import CORS



application = Flask(__name__)
CORS(application)

@application.route("/employees")
def index():
    employees = sql_lite_db.list_employees()
    return employees

@application.route("/employees/add")
def add(): 
    sql_lite_db.add_employee(firstName,lastName,emailId)
if __name__=="__main__":
    sql_lite_db.create_employee_table()
    application.run()
