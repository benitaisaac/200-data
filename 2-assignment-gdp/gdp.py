import csv
import json
import os
import pandas

BASE_DIR = os.path.dirname(__file__)


out_file_name = "all_countries.json"
gdp_csv_file = BASE_DIR + "/" + "gdp.csv"
gdp_csv_file_deleted = BASE_DIR + "/" "deleted_info.csv"

def save_file(dict_entries):
    with open(out_file_name, "w") as file:
        json.dump(dict_entries, file, indent=4)

# TODO: Make sure user can update the memory and original file without duplicate entries 

def del_entry(country_dict, country_slug, gdp_file, gdp_deleted_file):
    deleted_slug = country_dict[country_slug]
    del country_dict[country_slug]
    write_gdp(country_dict, gdp_file)
    all_deleted_countries = {}
    if os.path.exists(gdp_deleted_file):
        deleted_countries = read_gdp(gdp_deleted_file)
        all_deleted_countries = deleted_countries
    # all_deleted_countries.update(deleted_slug)
    all_deleted_countries[country_slug] = deleted_slug
    write_gdp(all_deleted_countries, gdp_deleted_file)

def update_slug(full_dict, s, val, ranking):
    full_dict[s]['value'] = val
    full_dict[s]['ranking'] = ranking
    write_gdp(full_dict, gdp_csv_file)

def combined_ppp(countries_dict):
    s1 = input("Enter first slug name: ")
    s2 = input("Enter second slug name: ")
    val_s1 = countries_dict[s1]['value'].replace("$", "").replace(",", "")
    val_s2 = countries_dict[s2]['value'].replace("$", "").replace(",", "")
    val_s1 = int(val_s1)
    val_s2 = int(val_s2)
    c_ppp = val_s1 + val_s2
    print(f"The combined PPP of {s1} and {s2} is ${c_ppp:,.2f}")

def display_slug(full_dict, s):
    print(full_dict[s])

def compare_slugs(countries_dict):
    s1 = input("Enter first slug name: ")
    s2 = input("Enter second slug name: ") 
    print(f"{s1}: Value: {countries_dict[s1]['value']} and Ranking: {countries_dict[s1]['ranking']} {s2} Value: {countries_dict[s2]['value']} and Ranking: {countries_dict[s2]['ranking']}")

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

def write_gdp(input_dict, file_name):
    data = []
    s = list(input_dict.keys())[0]
    d = input_dict[s]
    h = d.keys()
    data.append(h)
    for r in input_dict.values():
        data.append(r.values())
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def merg_files(file_1, file_2):
    #print(f"***File 1: {file_1}")
    #print(f"***File 2: {file_2}")

    f1 = pandas.read_csv(file_1)
    f2 = pandas.read_csv(file_2)
    merged_file = pandas.merge(f1, f2, how='outer', sort=True)
    #print(f"****merged file is: {merged_file}")
    merged_file.to_csv(gdp_csv_file, index=False)

def main():
    all_countries = read_gdp(gdp_csv_file)

    while True:
        choice = input('''
                    1. Display Details of slug
                    2. Update a slug 
                    3. Delete a slug
                    4. Compare two slugs
                    5. View Combined PPP
                    6. Merge Files 
                    e. Exit
                    
                    Enter Your Choice: ''')
        if choice not in ['1', '2', '3', '4', '5', '6', 'e']:
            print("Invalid choice.")
            continue
        
        if choice == '1':
            sluggy = get_slug_name()
            display_slug(all_countries, sluggy)
        elif choice == '2':
            sluggy = get_slug_name()
            val = input("Please type in new value: ")
            rank = input("Please type in new ranking: ")
            update_slug(all_countries, sluggy, val, rank)
        elif choice == '3':
            sluggy = get_slug_name()
            del_entry(all_countries, sluggy, gdp_csv_file, gdp_csv_file_deleted)
        elif choice == '4':
            compare_slugs(all_countries)
        elif choice == '5':
            combined_ppp(all_countries)
        elif choice == '6':
            merg_files(gdp_csv_file, gdp_csv_file_deleted)
            all_countries = read_gdp(gdp_csv_file)
        elif choice == 'e':
            break

main()