import sqlite3
from _functions import query_vehicle_with_


def go_fetch_all():   
    conn = sqlite3.connect('db\SQLiteDB.db')
    cursor = conn.cursor()
    result = cursor.execute('select * from persons;').fetchall()
    return result

class Person:
    
    def __init__(self, firstname, lastname, birthdate, address):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address
     
    def __str__(self):
        return f"{self.firstname} {self.lastname} is born {self.birthdate} and lives on {self.address}"

    def people_print():
        try:
            
            fetch_all_result = go_fetch_all()
            lst_of_lst = list(map(list, fetch_all_result))
            len_of_lst_of_lst = len(lst_of_lst)
            
            for i in range(len_of_lst_of_lst):
                person = lst_of_lst[i]
                person_finished = Person(person[0], person[1], person[2], person[3])
                print(person_finished)
        except IndexError as error:
            print("Woops -", error)
            
            
            
class Car_owned:
    
    def __init__(self, manufacturer, model, color, regnr, owner):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.regnr = regnr
        self.owner = owner
     
    def __str__(self):
        return f"The owner of the {self.color} {self.manufacturer} {self.model} with registration number {self.regnr} is {self.owner}"

    def car_print():
        try:
            
            fetch_all_result = query_vehicle_with_()
            lst_of_lst = list(map(list, fetch_all_result))
            len_of_lst_of_lst = len(lst_of_lst)
            
            for i in range(len_of_lst_of_lst):
                vehicle = lst_of_lst[i]
                vehicle_finished = Car_owned(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4])
                print(vehicle_finished)
        except IndexError as error:
            print("Woops -", error)