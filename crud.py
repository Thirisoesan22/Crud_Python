import sqlite3

if __name__=="__main__":
    connection=sqlite3.connect("unidb.db")
    cursor=connection.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS unitable(name VARCHAR(20),rollno TEXTVARCHAR(20), major VARCHAR(20), phone INTEGER)''')

def insert_data(name,rollno,major,phone):  
    try:
        sql = "INSERT INTO unitable (name,rollno,major,phone) VALUES (?,?,?,?)"
        values = (name,rollno,major,phone)
        cursor.execute(sql, values)
        print("Record inserted successfully")
    except Exception as e:
        print(e)
        connection.rollback()
    connection.commit()

def read_data():
    sql = "SELECT * FROM unitable"
    cursor.execute(sql)
    records = cursor.fetchall()
    for x in records:
        print(x)

# read_data()
    

def update_data(old_rno,new_rno):
    sql = "Update unitable SET rollno=? where rollno=?"
    values=(new_rno,old_rno)
    cursor.execute(sql, values)
    
    connection.commit()
    print("Record updated successfully")

update_data("2ICT-8","1ICT-13")
    

def delete_data(new_rollno):
  sql = "DELETE FROM unitable WHERE rollno = ?"
  cursor.execute(sql, (new_rollno,))
  connection.commit()
  print("Record deleted successfully")

# delete_data("2EC-7")
   
# name="Kyaw Kyaw"
# rollno="2ICT-12"
# major="ICT"
# phone="098367764874"
# insert_data(name,rollno,major,phone)


option = input("1 to Insert , \n 2 to Delete , \n 3 to Update : ")
if option=='1':
    name=input("Name:")
    rollno=input("Rollno:")
    major=input("Major:")
    phone=input("Phone:")
    insert_data(name,rollno,major,phone)

elif option=='2':
    rno=input("Type the roll no u want to delete :")
    delete_data(rno)

elif option=='3':
    o_rno=input("old roll no :")
    n_rno=input("new roll no :")
    update_data(o_rno,n_rno)

else:
    print("Error")