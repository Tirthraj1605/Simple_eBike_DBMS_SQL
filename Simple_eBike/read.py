from database import view_all_data, view_only_dealer_names, get_dealer
import pandas as pd

def read():
    print("1. View complete table")
    print("2. View dealer names")
    print("3. Select particular dealer by name")
    op = int(input("Enter your choice: >"))
    if op == 1:
        # print(view_all_data())
        rows = view_all_data()
        df = pd.DataFrame(rows, columns=['Dealer ID    ', 'Dealer Name   ', 'Dealer City   ', 'Dealer Pin     ', 'Dealer Street'])
        print(df)
        # for i in rows:
        #     print(i)
        
    elif op == 3:
        name = input("Enter dealer name: >")
        # print(get_dealer(name))
        rows = get_dealer(name)
        for i in rows:
            print(i)
    else:
        # print(view_only_dealer_names())
        data = view_only_dealer_names()
        print(pd.DataFrame(data, columns=['Dealer name']))
        # for i in data:
        #     print(i)
