import os
import pymysql
import os
from dotenv import load_dotenv
import time


def read(Table_name):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    port = os.environ.get("mysql_port")
    
    l=[]
    
    try:
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
        
        try:
            cursor.execute(f'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{Table_name}" ORDER BY ORDINAL_POSITION')
            rows = cursor.fetchall()
            
            key = []
            for row in rows:
                key.append(str(row[0]))

            cursor.execute(f'SELECT * FROM {Table_name}')
            if Table_name == "orders":
                pass
            else:
                rows = cursor.fetchall()

                l = [{key[k]: row[k] for k in range(0,len(key))} for row in rows]
            
        except pymysql.err.ProgrammingError:
            if Table_name == "products":
                print(f"No {Table_name} table in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`price` float NULL, UNIQUE (`name`))")
                time.sleep(2)
            if Table_name == "couriers":
                print(f"No {Table_name} data in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`phone` int NULL, UNIQUE (`name`))")
                time.sleep(2)
            if Table_name == "orders":
                print(f"No {Table_name} data in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`customerid` int NOT NULL,`courierid` int NOT NULL, FOREIGN KEY (customerid) REFERENCES customers(id), , FOREIGN KEY (courierid) REFERENCES couriers(id))")
                
                time.sleep(2)
    except pymysql.err.OperationalError:
        print(f"No {Table_name} data in the system. A new empty table is being created")
        time.sleep(2)
        
        connection = pymysql.connect(
            host,
            user,
            password,
            port = int(port) 
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE `app`")
        cursor.execute("USE `app`")
        cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`price` float NULL, UNIQUE (`name`))")
        
    connection.commit()
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()
                
    return l

read("products")