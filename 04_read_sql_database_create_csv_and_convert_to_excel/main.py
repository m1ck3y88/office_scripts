import pandas as pd
import psycopg2
import csv

'''
This scripts connects to an example PostgreSQL database called 'dvdrental',
pulls data from a table called 'customer', creates a csv file called 
'customers.csv' then converts it to an Excel file called 'customers.xlsx'.
I've included the compressed database file in this directory for download.
This way you can practice running queries on it after importing it to your
own local SQL environment. Note that if you want to perform the same actions
demonstrated in this script, you will have to delete the 'customers.csv' and
and 'customers.xlsx' files before running this script. Make sure to update the
credentials for the database connection to match whatever you set them to in your 
local environment.
'''

def get_connection():
    """
    Connects to the PostgreSQL database.
    :return: PostgreSQL connection
    """
    try:
        return psycopg2.connect(
            database='dvdrental',
            user='postgres',
            password='password',
            host='127.0.0.1',
            port=5432,
        )
    except:
        return False
conn = get_connection()
if conn:
    print('Connection to the PostgreSQL established successfully.')
else:
    print('Connection to the PostgreSQL encountered and error.')

# get the connection object
conn = get_connection()
# create a cursor using the connection object
curr = conn.cursor()
# execute the sql query
curr.execute('SELECT * FROM customer;')
# fetch all the rows from the cursor
data = curr.fetchall()
# close connection
conn.close()

# Write into CSV Files Using csv.writer()

# field names
fields = [
    'customer_id',
    'store_id',
    'first_name',
    'last_name',
    'email',
    'address_id',
    'active_bool',
    'create_date',
    'last_update',
    'active'
]

# name of csv file
filename = 'customers.csv'

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(data)

# Convert CSV to Excel using Pandas

# Reading the csv file
df_new = pd.read_csv('customers.csv')

# writing to xlsx file
xlsx_file = pd.ExcelWriter('customers.xlsx')
df_new.to_excel(xlsx_file, index=False)

xlsx_file.close()