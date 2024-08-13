from database import add_data

def create():
    dealer_id = int(input("Enter dealer id: >"))
    dealer_name = input("Enter dealer name: >")
    dealer_city = input("Enter dealer city: >")
    dealer_pin = input("Enter pin code: >")
    dealer_street = input("Enter street name: >")

    add_data(dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
    print('Data successfully added!')
