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
    
    dummy_k = []
    dummy_v = []
    
    for k, v in d.items():
        if v:
            dummy_k.append(k)
            dummy_v.append(v)
        else:
            d[k] = None
            
    k = (', '.join(str(key) for key in dummy_k))
    v = (', '.join("'" + str(value) + "'" for value in dummy_v))

    cursor.execute(f"INSERT INTO {string} ({k}) VALUES ({v});")
    connection.commit()
    
    cursor.execute(f"SELECT id FROM {string} WHERE {string}.name = '{d['name']}'")
    d['id'] = int((cursor.fetchall())[0][0])
    key_order = ["id"]
    for key in d: key_order.append(key)
    d = {k : d[k] for k in key_order}
    
    cursor.close()
    connection.close()
    
    return d

def edit_item_table(id, d = dict(), key = str, string = "products"):
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

    cursor.execute(f"UPDATE {string} SET {string}.{key} = '{d[key]}' WHERE {string}.id = '{id}';")
    connection.commit()
    
    cursor.close()
    connection.close()
    
def delete_item_table(id, string = "products"):
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

    cursor.execute(f"DELETE FROM `{string}` WHERE ((`id` = '{id}'));")
    connection.commit()
    
    cursor.close()
    connection.close()  
    