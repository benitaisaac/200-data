import csv
import json

out_file_name = "all_countries.json"

#create functions to call in main()
def save_file(dict_entries):
    with open(out_file_name, "w") as file:
        json.dump(dict_entries, file, indent=4)
        
def read_file():
    with open(out_file_name, "r") as file:
        data = json.load(file)
        return data

def del_entry(country_dict, country_slug):
    del country_dict[country_slug]

def update_slug(full_dict, s, val, ranking):
    full_dict[s]['value'] = val
    full_dict[s]['ranking'] = ranking

def display_slug(full_dict, s):
    print(full_dict[s])

def get_slug_name():
    s = input("Enter a slug name: ")
    return s

def read_gdp(file_name):
    full_dict = {}
    with open(file_name, newline='') as gdpfile:
        gdp_rows = csv.DictReader(gdpfile)
        for gpd_row in gdp_rows:
            full_dict[gpd_row['slug']] = gpd_row
    return full_dict

def main():
    all_countries = read_gdp('gdp.csv')

    while True:
        choice = input('''
                    1. Display Details of slug
                    2. Update a slug 
                    3. Delete a slug
                    4. Update a slug
                    e. Exit
                    
                    Enter Your Choice: ''')
        if choice not in ['1', '2', '3', '4', 'e']:
            print("Invalid choice.")
            continue
        
        if choice == '1':
            sluggy = get_slug_name()
            display_slug(all_countries, sluggy)
        if choice == '2':
            sluggy = get_slug_name()
            val = input("Please type in new value: ")
            rank = input("Please type in new ranking: ")
            update_slug(all_countries, sluggy, val, rank)
        elif choice == 'e':
            break

main()
    





