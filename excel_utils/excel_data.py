from openpyxl import load_workbook

# Functions to help grab and write excel data to xlsx files

def get_excel_sheet(location, worksheet):
    excel_file = load_workbook(filename = location)
    excel_sheet = excel_file[worksheet]
    return excel_sheet
