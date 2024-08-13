from database import delete_data

def delete():
    name = input("Enter the name of the dealer u want to delete: >")
    delete_data(name)
    print("Successfully deleted the dealer ", name)

