def display_menu():
    print("Command Menu")
    print("view   ---> View country name")
    print("add    ---> Add a country")
    print("delete ---> Delete a country")
    print("exit   ---> Exit the program")
    print()


def prepopulate_countries():
    countries = {
        "USA": "United States",
        "CAN": "Canada",
        "AUS": "Australia"
    }
    return countries

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "country codes:  "
    for code in codes:
        codes_line += code + "  "
    print(codes_line)
        
def view(countries):
    display_codes(countries)
    code = input("Enter the code of the country you want to view: ").upper()
    if code in countries:
        name = countries.pop(code)
        print(f"Country name: {name}. \n")
    else:
        print("There is no coutry with that code. \n")
        
def add(countries):
    code = input("Enter the code of the new country: ").upper()
    if code in countries:
        print(f"Country with code, {code}, already exists. \n")
    else:
        name = input("Enter the name of the new country: ").upper()
        countries[code] = name
        print(f"Country, {name}, added successfully. \n")

def delete(countries):
    code = input("Enter the code of the country you want to delete: ").upper()
    if code in countries:
        name = countries.pop(code)
        print(f"Country, {name} deleted successfully. \n")
    else:
        print("Invalid key. \n")

def main():
    countries = prepopulate_countries()
    display_menu()
    while True:
        Command = input("Command: ").lower()
        if Command == "view":
            view(countries)
        elif Command == "add":
            add(countries)
        elif Command == "delete":
            delete(countries)
        elif Command == "exit":
            print("Bye.")
            break
        else:
            print("Invalid command. Please try again. \n")


if __name__ == "__main__":
    main()
