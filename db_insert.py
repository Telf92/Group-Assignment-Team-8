import sqlite3
import csv

file_path = input("Please enter the file path: ")
# r"C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv"

try:
  
    # Import csv and extract data, this is where we need to start. 
    # Basicly open up the CSV file and importing the raw text into the DB
    with open(file_path, 'r') as fin:
        dict_reader = csv.DictReader(fin)
        persons = [(i['Firstname'], i['Lastname'], i["Birthdate"], i["Address"]) for i in dict_reader]
        # print(persons)
  
    # Connect to SQLite. 
    # This creates the connection to the database, which is needed to make changes to it. Its not the same as writing a textfile or w/e
    sqliteConnection = sqlite3.connect(r"C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\db\SQLiteDB.db")
    cursor = sqliteConnection.cursor()
  
    # Create the table 
    # This is where we create the table
    cursor.execute('create table persons(firstname, lastname , birthdate, address);')
  
    # Insert data into table. 
    # And this is where the data from the persons.csv file get imported
    cursor.executemany("insert into persons (firstname, lastname , birthdate, address) VALUES (?, ?, ?, ?);", persons)
  
    # Show the table
    cursor.execute('select * from persons;')
  
    # View result
    # result = cursor.fetchall()
    # print(result)
  
    # Commit work and close connection. 
    # Think Git :') 
    # We need to commit our changes to the database for it in order for it to get updated weith the new information
    sqliteConnection.commit()
    cursor.close()
    
except sqlite3.Error as error:
        print('Error occured - ', error)
except FileNotFoundError as error2:
    print("Wrong path specified -", error2)
 

try:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')
except NameError as error3:
    print("Wrong path specified -", error3)
    