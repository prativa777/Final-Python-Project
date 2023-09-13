# If we want to connect database from a program (python, js) then we need a database connector
# Database connecter connects your program with Database msqclient, psyclient, etc. are db connectors

def estd_connection():
    import psycopg2
    conn=psycopg2.connect(
        database='student',
        user='sana',
        password='12345',
        host= 'localhost',
        port='5432'
    )

    conn.autocommit= True
    print("connection established successfully!")
    cursor=conn.cursor()
    return cursor


if __name__=="__main__":
    estd_connection()
