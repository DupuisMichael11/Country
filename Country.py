#Michael_Dupuis_CIS261_WK4_Country

def display_menu():
    print("Command Menu")
    print("view - View Country Name")
    print("add - Add Country")
    print("delete - Delete Country")
    print("exit - Exit Program\n")
    
def populate_codes(countries):
    codes = list(countries)
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)
    
def view(countries):
    populate_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print(f"There is no country with that code.\n")
        
def add_country(countries):
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"That {name} is already using that code")
    else:
        name = input("Enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} has been added.\n")
        
def del_country(countries):
    code = input("Enter Country Code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted")
    else:
        print("There is no country with that code.\n")
        
def main():
    countries = {"US": "United States of America", "GB": "United Kingdom", "CN": "China"}
    
    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add_country(countries)
        elif command == "delete":
            del_country(countries)
        elif command == "exit":
            print("Have a good day.\n")
            break
        else:
            print("Invalid command entered, please try again: \n")
        
if __name__ == "__main__":
    main()
    
      
    
