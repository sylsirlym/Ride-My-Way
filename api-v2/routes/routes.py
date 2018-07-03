import os
from flask import Flask,jsonify,request, make_response, abort
import json
import psycopg2

app = Flask (__name__)

def connectDB():
    
    #Define a connection string
    conn_string = "host='localhost' dbname='ridemyway' user='postgres' password='Secrets'"
    
    #Initialize a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
        #conn.cursor will return a cursor object, used to perform queries
    cursor = conn.cursor()
    print ("Connected!\n")
    conn.close()


if __name__ == '__main__':
    connectDB()
    # app.run(debug=True)