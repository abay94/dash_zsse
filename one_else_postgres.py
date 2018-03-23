#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
# dbname = input("Enter the name of the data base")
# user = input("Enter the user")
# passwrd = input("Enrter the password")
# host = input("Please enter the host: ")
# connection_string = "dbname=" + str(dbname) + " " + "user=" + str(
#     user) + " " + "host=" + host + " " + "password=" + passwrd
try:
    conn = psycopg2.connect("dbname='zsse' user='postgres' host='192.168.1.92' password='postgres'")
    # conn = psycopg2.connect(connection_string)
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("""SELECT temp from warehouse_ana""")
rows = cur.fetchall()
print ("\nShow me the databases:\n")
for row in rows:
    print ("   ", row[0])

print(len(rows))
print(rows[len(rows) - 1])
print(type(rows))

#
# Enter the user'postgres'
# Enrter the password'postgres'
# Please enter the host: '192.168.1.92'