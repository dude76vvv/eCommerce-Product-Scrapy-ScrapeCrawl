from prettytable import from_db_cursor
import mysql.connector
from dotenv import  dotenv_values,load_dotenv,find_dotenv
import os

load_dotenv()

dbConn = {
    'host': os.environ['HOST'],
    'database': os.environ['DB_NAME'],
    'user': os.environ['USER'],
    'password': os.environ['PASSWORD']
}

#display with pretty table

try:

    conn=mysql.connector.connect(**dbConn)

    with conn:
        cur = conn.cursor()
        cur.execute('SELECT title,price from switchgames')
        x = from_db_cursor(cur)
        x.align = "l"
        print(x)

except Exception as e:
    print(e)







