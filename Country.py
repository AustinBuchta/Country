def display_menu():
    print("=== COUNTRY DICTIONARY ===")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")

def populate_dictionary():
    countries = {"1": "United States", "2": "United Kingdom", "3": "France"}
    return countries

def view_country(dictionary):
    print("Available countries:")
    for key in dictionary:
        print(key, "-", dictionary[key])
    user_input = input("Enter the key of the country you want to view: ")
    if user_input in dictionary:
        print("Country:", dictionary[user_input])
    else:
        print("Invalid key!")

def add_country(dictionary):
    key = input("Enter the key for the new country: ")
    if key in dictionary:
        print("Country with this key already exists!")
    else:
        country = input("Enter the name of the new country: ")
        dictionary[key] = country
        print("Country added successfully!")

def delete_country(dictionary):
    print("Available countries:")
    for key in dictionary:
        print(key, "-", dictionary[key])
    key = input("Enter the key of the country you want to delete: ")
    if key in dictionary:
        del dictionary[key]
        print("Country deleted successfully!")
    else:
        print("Invalid key!")

def main():
    countries_dict = populate_dictionary()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_country(countries_dict)
        elif choice == "2":
            add_country(countries_dict)
        elif choice == "3":
            delete_country(countries_dict)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
