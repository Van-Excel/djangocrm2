# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Technicalking1.',

)
# prepare cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute('CREATE DATABASE crm2')

print('All done')
