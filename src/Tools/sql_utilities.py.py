import os
import pymysql
import os
from dotenv import load_dotenv

def add_item_table(d = dict(), string = "products"):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    port = os.environ.get("mysql_port")
    
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database,
        port = int(port) 
    )
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()

    k = (', '.join(str(key) for key in d.keys()))

    v = (', '.join("'" + str(value) + "'" for value in d.values()))

    cursor.execute(f"INSERT INTO {string} ({k}) VALUES ({v});")
    connection.commit()
    
    cursor.execute(f"SELECT id FROM {string} WHERE {string}.name = '{d['name']}'")
    d['id'] = int((cursor.fetchall())[0][0])
    print(d['id'])
    
    cursor.close()
    connection.close()
    
    return d
    