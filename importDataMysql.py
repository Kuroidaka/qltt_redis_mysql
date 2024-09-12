import pandas as pd
import mysql.connector
from mysql.connector import Error

# Read the CSV file into a pandas DataFrame
file_path = './FastFoodRestaurants.csv'
df = pd.read_csv(file_path)

# Replace NaN values with None
df = df.where(pd.notnull(df), None)

# Establish a connection to the MySQL database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Insert data into the table
def insert_data_to_db(connection, df, table_name):
    cursor = connection.cursor()
    # Insert data row by row
    for _, row in df.iterrows():
        sql = f"""
        INSERT INTO {table_name} (id, address, city, country, keysData, latitude, longitude, name, postalcode, province, websites)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            None,  # id (assuming AUTO_INCREMENT)   
            row['address'],
            row['city'],
            row['country'],
            row['keys'],
            row['latitude'],
            row['longitude'],
            row['name'],
            row['postalCode'],
            row['province'],
            row['websites']
        )
        cursor.execute(sql, values)
    connection.commit()

# Provide your database details here
connection = create_connection("localhost", "root", "Idaka123", "phamdoancanh")

# Replace 'your_table_name' with your actual table name
insert_data_to_db(connection, df, 'restaurant')

# Close the connection
if connection.is_connected():
    connection.close()
    print("The connection is closed")
