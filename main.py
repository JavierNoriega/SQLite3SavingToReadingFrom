from database import show_db_records, sqlite_create_db, create_cur, create_con
import pyinputplus as pyip

connection = create_con()
cursor = create_cur()


def start():
    enter_new_record = pyip.inputChoice(['y', 'n'], prompt="Would you like to enter a new record? (y/n): ")

    if enter_new_record == 'y':
        sqlite_create_db()
        person_eyes = str(input("Enter the person's eye color: ").capitalize())
        person_hair = str(input("Enter the person's hair color: ").capitalize())
        person_gender = str(input("Enter the person's gender: ").capitalize())

        cursor.execute('SELECT * FROM personsZ WHERE eyes = ? AND hair = ? AND gender = ?', (person_eyes, person_hair, person_gender))
        person_exists = cursor.fetchone()

        if person_exists:
            print("Person Exists")
        else:
            cursor.execute('INSERT INTO personsZ VALUES (?, ?, ?)', (person_eyes, person_hair, person_gender))
            print("New Person Added")

        connection.commit()
        connection.close()

    else:
        view_records()


def view_records():

    view_existing = pyip.inputChoice(['y', 'n'], "Would you like to view our persons stored? (y/n): ")
    if view_existing == 'y':

        order = pyip.inputChoice(['1', '2', '3'], "Type 1 to order by Eye Color, 2 for Hair Color, and 3 for Gender: ")
        show_db_records(order)

    else:
        print("GoodBye!")


start()
