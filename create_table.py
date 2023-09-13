from connection_estd import estd_connection

cursor=estd_connection()
sql="""
    CREATE TABLE USERINFORMATION(
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    TITLE CHAR(10),
    AGE INT,
    NATIONALITY CHAR(30),
    NOOFCOURSES INT,
    NOOFSEM INT,
    REGISTRATION_STATUS varchar
    )""" 
    
    
cursor.execute(sql) 
print("table created successfully!") 