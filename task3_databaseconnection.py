import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Svkm@2019$",
  database="employee_management"
)

mycursor = mydb.cursor()

def add_employee(name, age, email):
    sql = "INSERT INTO employees (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    mycursor.execute(sql, val)
    mydb.commit()
print(mycursor.rowcount, "record inserted sucessfully...........")

def view_employees():
  mycursor.execute("SELECT * FROM employees")
  myresult = mycursor.fetchall()
  for employee in myresult:
      print(employee)

def main():
    add_employee("gaurav11' ",21, "gaurav11@gmail.com")
    view_employees()


if __name__ == '__main__':
    main()



