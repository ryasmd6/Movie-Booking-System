import mysql.connector

con = mysql.connector.connect(host="localhost:3306", user="root", password="root", database="dbtheatre")

def create_table(con):
    cursor=con.cursor() 
    create_table_query =("CREATE TABLE IF NOT EXISTS  users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50)  NOT NULL,age VARCHAR(100) NOT NULL,city VARCHAR(20) NOT NULL)")
    cursor.execute(create_table_query)	     
    con.commit()
    print("Table 'users' created sucessFully.")
if __name__== "__main__":
    create_table(con)