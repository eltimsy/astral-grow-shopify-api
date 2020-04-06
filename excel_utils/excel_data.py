from openpyxl import load_workbook

from excel_utils.excel_consts import COST_ROW, PRICE_ROW
# Functions to help grab and write excel data to xlsx files


class Store:
    ''' One of the stores '''

    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, variant_id, product_id, name, cost, price, row_id):
        self.products[name] = Product(variant_id, product_id, name, cost, price, row_id)
        return self.products[name]

    def change_product(self, name, cost, price, worksheet):
        ''' Function to grab product and run edit product method'''

        try:
            existing_product = self.products[name]
        except KeyError:
            return print('Does not exist')

        updated_product = existing_product.edit_product(cost, price, worksheet)
        return updated_product


class Product:
    ''' Template for each prdocut row in excel file '''

    def __init__(self, variant_id, product_id, name, cost, price, row_id):
        self.variant_id = variant_id
        self.product_id = product_id
        self.name = name
        self.cost = cost
        self.price = price
        # This is the row number of the line in excel
        self.row_id = str(row_id)

    def edit_product(self, cost, price, worksheet):
        self.cost = cost
        self.price = price
        worksheet[COST_ROW + self.row_id] = cost
        worksheet[PRICE_ROW + self.row_id] = price
        return self


def get_excel_data(location, worksheet):
    ''' Grab the worksheet based on where the file and name of the worksheet '''

    excel_file = load_workbook(filename=location)
    excel_sheet = excel_file[worksheet]
    return excel_file, excel_sheet


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
                row[0].row,
            )

    return current_store
