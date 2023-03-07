import sqlite3
 
def get_database_connexion():
    con = sqlite3.connect("employee.db")
    return con
 
def create_employee_table():
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName VARCHAR(15),
                lastName VARCHAR(15),
                emailId VARCHAR(25)
    );
            """
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
 
def list_employees():
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ SELECT id, firstName, lastName, emailId
                FROM employees
                ORDER BY firstName, lastName ASC;
            """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result
 
def load_employee(employee_id):
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ SELECT id, firstName, lastName, emailId
                FROM employees
                WHERE id = ?;
            """
    cursor.execute(query,(employee_id))
    result = cursor.fetchone()
    cursor.close()
    con.close()
    return result
 
def add_employee(firstName, lastName, emailId):
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ INSERT INTO employees(firstName, lastName, emailId)
                VALUES(?, ?, ?);
            """
    cursor.execute(query,(firstName, lastName, emailId))
    con.commit()
    cursor.close()
    con.close()
 
def delete_employee(employee_id):
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ DELETE
                FROM employees
                WHERE id = ?;
            """
    cursor.execute(query,(employee_id))
    con.commit()
    cursor.close()
    con.close()
 
def update_employee(employee_id, firstName, lastName,emailId):
    con = get_database_connexion()
    cursor = con.cursor()
    query = """ UPDATE employees
                SET firstName = ? ,lastName = ? , emailId = ?
                WHERE id = ?;
            """
    cursor.execute(query,(firstName, lastName, emailId,employee_id))
    con.commit()
    cursor.close()
    con.close()
    