from configparser import ConfigParser

import pyodbc 
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=myserver;Database=mydatabase;Port=4321;User ID=myuserid;Password=mypassword')
