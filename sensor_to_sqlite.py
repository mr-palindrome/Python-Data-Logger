import serial
import sqlite3
import psutil as ps
import time
try:
    dbConn = sqlite3.connect('datalogger.db')
except:
    print("could not connect to database")
#open a cursor to the database
cursor = dbConn.cursor()

device = 'COM18' #this will have to be changed to the serial port you are using
try:
  print("Trying...",device)
  arduino = serial.Serial(device, 9600) 
except: 
  print("Failed to connect on",device)

while True:
    try:
      time.sleep(2)
      data = arduino.readline()  #read the data from the arduino
      print(data)
      pieces = data.split(" ")  #split the data by the tab
      #Here we are going to insert the data into the Database
      try:
        cursor.execute("INSERT INTO sensor_data VALUES (?,?,?,?,?)", (pieces[0],pieces[1],pieces[2],pieces[3],pieces[4]))
        dbConn.commit() #commit the insert
      except sqlite3.IntegrityError:
        print("failed to insert data")
#      finally:
#        cursor.close()  #close just incase it failed
    except:
      print("Failed to get data from Arduino!")