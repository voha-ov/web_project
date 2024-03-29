import pyodbc

# for driver in pyodbc.drivers():
#     print(driver)

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-NV529A0\SQLEXPRESS;"
                      "Database=test;"
                      "Trusted_Connection=yes"
                      )
# Check for connection
if cnxn:
    print("Connected")

cursor = cnxn.cursor()
cursor.execute("SELECT top 2 Price, ProductName \
                FROM tblProducts \
                WHERE Package_QTY > 5 \
                Order by Price desc")

for row in cursor:
    print(row)
