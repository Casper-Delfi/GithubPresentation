import pyodbc

# Connection parameters
server = 'your_server_address'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Connection string
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Connect to the database
    connection = pyodbc.connect(connection_string)
    
    # Create a cursor
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT @@version;")
    
    # Fetch and print the result
    row = cursor.fetchone()
    print("SQL Server version:", row[0])

    # Close the cursor and connection
    cursor.close()
    connection.close()

except pyodbc.Error as e:
    print("Error connecting to the database:", e)

