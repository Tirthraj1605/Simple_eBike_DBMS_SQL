from database import create_table, close
from create import create
from delete import delete
from read import read
from update import update

create_table()
print("**Welcome**")
def menu():
    while True:
        print(
            '''
            1. Add new data
            2. Delete data
            3. Read data
            4. Update data
            '''
        )
        op = int(input("Your choice: >"))

        if op == 1:
            create()
        elif op == 2:
            delete()
        elif op == 4:
            update()
        elif op == 3:
            read()
        else:
            close()
            exit()

menu()
