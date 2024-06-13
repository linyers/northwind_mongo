import csv
import json

CSV_FILE_PATH = './northwind_csv/'
JSON_FILE_PATH = './northwind_json/'

def convert_orders_csv_to_json():
    orders = []

    with open(CSV_FILE_PATH + "orders.csv", mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            orders.append(row)

    with open(CSV_FILE_PATH + "orders_details.csv", mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for order in orders:
                if order['orderid'] != row['orderid']:
                    continue
                
                if 'products' not in order:
                    order['products'] = []

                new_row = row.copy()
                new_row.pop('orderid')

                order['products'].append(new_row)

    with open(JSON_FILE_PATH + "orders.json", 'w', encoding='utf-8') as jsonfile:
        json.dump(orders, jsonfile, ensure_ascii=False, indent=4)

def convert_employees_csv_to_json():
    employees = []

    with open(CSV_FILE_PATH + "employees.csv", mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            employees.append(row)

    with open(CSV_FILE_PATH + "employee_territories.csv", mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for employee in employees:
                if employee['employeeid'] != row['employeeid']:
                    continue
                
                if 'territories' not in employee:
                    employee['territories'] = []

                employee['territories'].append(row['territoryid'])

    with open(JSON_FILE_PATH + "employees.json", 'w', encoding='utf-8') as jsonfile:
        json.dump(employees, jsonfile, ensure_ascii=False, indent=4)


def convert_csv_to_json(file_path_csv, file_path_json):
    data = []

    with open(file_path_csv, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(file_path_json, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    convert_orders_csv_to_json()
    convert_employees_csv_to_json()
    convert_csv_to_json(CSV_FILE_PATH + "products.csv", JSON_FILE_PATH + "products.json")
    convert_csv_to_json(CSV_FILE_PATH + "suppliers.csv", JSON_FILE_PATH + "suppliers.json")
    convert_csv_to_json(CSV_FILE_PATH + "categories.csv", JSON_FILE_PATH + "categories.json")
    convert_csv_to_json(CSV_FILE_PATH + "customers.csv", JSON_FILE_PATH + "customers.json")
    convert_csv_to_json(CSV_FILE_PATH + "regions.csv", JSON_FILE_PATH + "regions.json")
    convert_csv_to_json(CSV_FILE_PATH + "shippers.csv", JSON_FILE_PATH + "shippers.json")
    convert_csv_to_json(CSV_FILE_PATH + "territories.csv", JSON_FILE_PATH + "territories.json")
