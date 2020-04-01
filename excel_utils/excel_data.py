from openpyxl import load_workbook

# Functions to help grab and write excel data to xlsx files

class Store:
    ''' One of the stores '''

    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, variant_id, product_id, name, cost, price):
        self.products[name] = Product(variant_id, product_id, name, cost, price)
        return self.products[name]


class Product:
    ''' Template for each prdocut row in excel file '''

    def __init__(self, variant_id, product_id, name, cost, price):
        self.variant_id = variant_id
        self.product_id = product_id
        self.name = name
        self.cost = cost
        self.price = price


def get_excel_sheet(location, worksheet):
    ''' Grab the worksheet based on where the file and name of the worksheet '''

    excel_file = load_workbook(filename = location)
    excel_sheet = excel_file[worksheet]
    return excel_sheet


def make_store(name, excel_sheet):
    ''' Build the store class with all the products included '''

    current_store = Store(name)
    rows = excel_sheet.rows

    # Skip first line since it is the headers
    next(rows)
    for row in rows:
        if row[0].value:
            current_store.add_product(
                row[0].value,
                row[1].value,
                row[2].value,
                row[3].value,
                row[4].value,
            )

    return current_store
