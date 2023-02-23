import mysql.connector

# establish connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

# create a cursor object to interact with the database
mycursor = mydb.cursor()

# function to insert data into the database
def insert_data():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    sql = "INSERT INTO students (name, age, email) VALUES (%s, %s, %s)"
    val = (name, age, email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

# function to update data in the database
def update_data():
    id = input("Enter student ID: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    sql = "UPDATE students SET name = %s, age = %s, email = %s WHERE id = %s"
    val = (name, age, email, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record updated.")

# function to fetch data from the database
def fetch_data():
    mycursor.execute("SELECT * FROM students")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# function to delete data from the database
def delete_data():
    id = input("Enter student ID: ")
    sql = "DELETE FROM students WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted.")

# menu-driven interface
while True:
    print("\nWelcome to the Student Database")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Fetch Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        insert_data()
    elif choice == "2":
        update_data()
    elif choice == "3":
        fetch_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
