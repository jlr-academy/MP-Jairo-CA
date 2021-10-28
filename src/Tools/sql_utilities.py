import os
import pymysql
from dotenv import load_dotenv
import time

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

def add_order_table(d = dict(), string = "products"):
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
            if not k == "product":
                dummy_k.append(k)
                dummy_v.append(v)
            else:
                products = d[k]
        else:
            d[k] = None

    k = (', '.join(str(key) for key in dummy_k))
    v = (', '.join("'" + str(value) + "'" for value in dummy_v))

    cursor.execute(f"INSERT INTO {string} ({k}) VALUES ({v});")
    cursor.execute("SELECT LAST_INSERT_ID();")
    order_id = (cursor.fetchall())[0][0]
    connection.commit()
    
    for i in range(0, len(products), 2):
        cursor.execute(f"INSERT INTO order_products (orderid, product, quantity) VALUES ({order_id}, '{products[i]}', '{products[i+1]}');")
        connection.commit()
        
        cursor.execute(f'SELECT products.quantity FROM products WHERE id = {products[i]} GROUP BY products.quantity')
        rows = cursor.fetchall()

        dummy_quantity =  float(rows[0][0]) - products[i+1]
        
        
        cursor.execute(f"UPDATE products SET products.quantity = '{dummy_quantity}' WHERE products.id = '{products[i]}';")
        connection.commit()
    
    
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
    
def edit_order_products(id, d = dict(), key = str, string = "order_products"):
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
    
    cursor.execute(f"DELETE FROM `{string}` WHERE ((`orderid` = '{id}'));")
    connection.commit()

    cursor.execute(f"UPDATE {string} SET {string}.{key} = '{d[key]}' WHERE {string}.orderid = '{id}';")
    
    for k in d.keys():
        if k == "product":
            products = d[k]
            
    for i in range(0, len(products), 2):
        cursor.execute(f"INSERT INTO order_products (orderid, product, quantity) VALUES ({id}, '{products[i]}', '{products[i+1]}');")
        connection.commit()
        
        cursor.execute(f'SELECT products.quantity FROM products WHERE id = {products[i]} GROUP BY products.quantity')
        rows = cursor.fetchall()

        dummy_quantity =  float(rows[0][0]) - products[i+1]
        
        
        cursor.execute(f"UPDATE products SET products.quantity = '{dummy_quantity}' WHERE products.id = '{products[i]}';")
        connection.commit()
    
    cursor.close()
    connection.close()
    
def delete_order(id):
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
    
    cursor.execute(f"DELETE FROM `order_products` WHERE ((`orderid` = '{id}'));")
    connection.commit()

    cursor.execute(f"DELETE FROM `orders` WHERE ((`id` = '{id}'));")
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
    
def fetch_orders(Table_name):
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
    l = []
    
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT {Table_name}.id, customers.name as customer_name, customers.adress  as customer_adress, customers.phone  as customer_phone, couriers.name as courier, {Table_name}.status FROM {Table_name} INNER JOIN customers ON customers.id = customer INNER JOIN couriers ON couriers.id = courier GROUP BY {Table_name}.id, customers.name, customers.adress, customers.phone, couriers.name, {Table_name}.status')
    rows = cursor.fetchall()
    
    key = [i[0] for i in cursor.description]
    
    l = [{key[k] : row[k] for k in range(0,len(key))} for row in rows]
    
    connection.commit()
    
    cursor.close()
    connection.close()  
    
    return l

def fetch_orders_details(id):
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
    l = []
    
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT products.name as products FROM order_products INNER JOIN products ON products.id = product WHERE orderid = {id} GROUP BY products.name')
    rows = cursor.fetchall()
        
    for row in rows: l.append(row[0])
    
    lid = []
    
    cursor.execute(f'SELECT product FROM order_products WHERE orderid = {id} GROUP BY product')
    rows = cursor.fetchall()
        
    for row in rows: lid.append(row[0])
    
    connection.commit()
    
    cursor.close()
    connection.close()  
    
    return l , lid

def fetch_orders_status(string = "Preparing"):
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
    l = []
    
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT orders.id, customers.name as customer_name, customers.adress  as customer_adress, customers.phone  as customer_phone, couriers.name as courier, orders.status FROM orders INNER JOIN customers ON customers.id = customer INNER JOIN couriers ON couriers.id = courier WHERE orders.status = "{string}" GROUP BY orders.id, customers.name, customers.adress, customers.phone, couriers.name, orders.status')
    rows = cursor.fetchall()
    
    key = [i[0] for i in cursor.description]
    
    l = [{key[k] : row[k] for k in range(0,len(key))} for row in rows]
    
    connection.commit()
    
    cursor.close()
    connection.close()  
    
    return l

def fetch_orders_courier(id):
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
    l = []
    
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT orders.id, customers.name as customer_name, customers.adress  as customer_adress, customers.phone  as customer_phone, couriers.name as courier, orders.status FROM orders INNER JOIN customers ON customers.id = customer INNER JOIN couriers ON couriers.id = courier WHERE orders.courier = "{id}" GROUP BY orders.id, customers.name, customers.adress, customers.phone, couriers.name, orders.status')
    rows = cursor.fetchall()
    
    key = [i[0] for i in cursor.description]
    
    l = [{key[k] : row[k] for k in range(0,len(key))} for row in rows]
    
    connection.commit()
    
    cursor.close()
    connection.close()  
    
    return l

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
                rows = cursor.fetchall()

                l = [{key[k]: row[k] for k in range(0,len(key))} for row in rows]
                for item in l:
                    
                    [x, lid] = fetch_orders_details(item["id"])
                    item["product"] = lid
                    
            else:
                rows = cursor.fetchall()

                l = [{key[k]: row[k] for k in range(0,len(key))} for row in rows]
            
        except pymysql.err.ProgrammingError:
            
            if Table_name == "products":
                print(f"No {Table_name} table in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`price` float NULL,`quantity` float NOT NULL, UNIQUE (`name`))")
                time.sleep(2)
            if Table_name == "couriers":
                print(f"No {Table_name} data in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`phone` int NULL, UNIQUE (`name`))")
                time.sleep(2)
            if Table_name == "orders":
                print(f"No {Table_name} data in the system. A new empty table is being created")
                cursor.execute(f"CREATE TABLE `customers`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(255) NOT NULL,`adress` varchar(255) NULL, `phone` int NULL, UNIQUE (`name`))")
                cursor.execute(f"CREATE TABLE `{Table_name}`(`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY, `customer` int NOT NULL, `courier` int NOT NULL, `status` varchar(255) NOT NULL, FOREIGN KEY (customer) REFERENCES customers(id), FOREIGN KEY (courier) REFERENCES couriers(id))")
                cursor.execute(f"CREATE TABLE `order_products`(`orderid` int NOT NULL,`product` int NOT NULL, `quantity` int NOT NULL, FOREIGN KEY (orderid) REFERENCES orders(id), FOREIGN KEY (product) REFERENCES products(id))")

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

# SELECT orders.id, customers.name, customers.adress, customers.phone, couriers.name as courier, orders.status
#   FROM orders
#      INNER JOIN customers
#        ON customers.id = customerid
#      INNER JOIN couriers
#        ON couriers.id = courierid
#        WHERE courierid = '4'
#        GROUP BY orders.id, customers.name, customers.adress, customers.phone, couriers.name, orders.status
# ;

# SELECT orders.id, customers.name, customers.adress, customers.phone, couriers.name as courier, orders.status
#   FROM orders
#      INNER JOIN customers
#        ON customers.id = customerid
#      INNER JOIN couriers
#        ON couriers.id = courierid
#        WHERE status= 'preparing'
#        GROUP BY orders.id, customers.name, customers.adress, customers.phone, couriers.name, orders.status
