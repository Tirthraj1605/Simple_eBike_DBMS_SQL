from database import edit_dealer_data, get_dealer_


def update():
    dealer_id = int(input("Enter the dealer id which you want to edit: >"))
    # 
    res = get_dealer_(dealer_id)
    if res:
        dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street = res[0][0],res[0][1],res[0][2],res[0][3],res[0][4]
    else:
        return
    print("current dealer that you have selected: ")
    print(res)
    # Get user input for the new values
    new_id = input("Enter new dealer id (or 0 to keep old value): ")
    new_name = input("Enter new dealer name (or 0 to keep old value): ")
    new_pin = input("Enter new dealer pin (or 0 to keep old value): ")
    new_city = input("Enter new dealer city (or 0 to keep old value): ")
    new_street = input("Enter new dealer street (or 0 to keep old value): ")

    new_id = dealer_id if new_id == '0' else new_id
    new_name = dealer_name if new_name == '0' else new_name
    new_pin = dealer_pin if new_pin == '0' else new_pin
    new_city = dealer_city if new_city == '0' else new_city
    new_street = dealer_street if new_street == '0' else new_street

    # query = 'update dealer set dealer_id=%s, dealer_name=%s, dealer_city=%s, dealer_pin=%s, dealer_street=%s where dealer_id=%s and dealer_name=%s and dealer_city=%s and dealer_pin=%s and dealer_street=%s'
    # param = (new_id, new_name, new_city, new_pin, new_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
    # print("checking query and paramas", query, param)
    # d = edit_dealer_data(query, param)

    data = edit_dealer_data(new_id, new_name, new_city, new_pin, new_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
    print("Successfully edited ", new_name)
