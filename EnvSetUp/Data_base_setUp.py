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
digits = []
txt = []

for row in cursor:
    txt.append(row[0])
    digits.append(row[1])
    # print(row[0], row[1])

print(digits,"\n",txt)
