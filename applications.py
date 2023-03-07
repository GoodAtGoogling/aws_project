import sqlite3

def get_database():
    con = sqlite3.connect("employee.db")
    return con

def create_table():
    con = get_database()
    cursor = con.cursor()
    query = """CREATE TABLE IF NOT EXISTS employees(
               id INTEGER PRIMARY KEY AUTOINCREMENT
               firstName VARCHAR(15)
               lastName  VARCHAR(15)
               emailId VARCHAR(25)
    );
                
             """
    cursor.execute(query)
    con.commit()
    con.close()
    cursor.close()
  
    

def list_employees():
    con = get_database()
    cursor = con.cursor()
    query = """SELECT id, firstName, lastName,emailId
                FROM employees
                ORDER BY firstName, lastName ASC;
             """
    cursor.execute(query)
    result = cursor.fetchall()
    con.close()
    cursor.close()
    return result

def list_employee(employee_id):
    con = get_database()
    cursor = con.cursor()
    query = """SELECT*
                FROM employees
                WHERE id=?;
             """
    cursor.execute(query,(employee_id))
    result = cursor.fetchone()
    con.close()
    cursor.close()
    return result


def add_employee():
    return None

def delete_employee():
    return None

def update_employee() : 
    return None
    