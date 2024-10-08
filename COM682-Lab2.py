import pyodbc

# Connection details
server = 'mycourse1234.database.windows.net'  # Replace with your actual server
database = 'myCourse'  # Replace with your actual database
username = 'azureuser'  # Replace with your actual username
password = 'Kyrieirving101'  # Replace with your actual password
driver = '{ODBC Driver 17 for SQL Server}'  # ODBC Driver version


# Establishing connection
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password) as conn:
    with conn.cursor() as cursor:
        # Execute query
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        
        # Fetch and print the results
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
