from openpyxl import load_workbook

from excel_utils.excel_data import Store
from excel_utils.excel_consts import (
    PROD_ID,
    VAR_ID,
    PROD_NAME,
    PROD_COST,
    PROD_PRICE,
    FBA_FEE,
    SEND_FEE,
)


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
            # TO FIX think of a way to use formulas
            if row[0].value == 'Combo':
                prod_cost = 26.69
            else:
                prod_cost = row[PROD_COST].value

            current_store.add_product(
                row[PROD_ID].value,
                row[VAR_ID].value,
                row[PROD_NAME].value,
                prod_cost,
                row[PROD_PRICE].value,
                row[FBA_FEE].value,
                row[SEND_FEE].value,
                row[PROD_ID].row,
            )

    return current_store
