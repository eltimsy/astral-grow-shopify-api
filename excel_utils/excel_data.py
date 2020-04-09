from excel_utils.excel_consts import COST_COL, PRICE_COL, MARGIN_TO_LOW
# Functions to help grab and write excel data to xlsx files


class Store:
    ''' One of the stores '''

    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(
        self, variant_id, product_id, name,
        cost, price, fba_fee, send_fee, row_id,
    ):
        amazon_fee = price * .15

        # TO FIX need to find a way to use formulas
        try:
            profit = price - amazon_fee - fba_fee - send_fee - cost
        except TypeError:
            profit = 0

        margin = profit / price
        self.products[name] = Product(
            variant_id, product_id, name, cost,
            price, amazon_fee, fba_fee, send_fee,
            profit, margin, row_id,
        )
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

    def __init__(
        self, variant_id, product_id, name, cost,
        price, amazon_fee, fba_fee, send_fee, profit,
        margin, row_id,
    ):
        self.variant_id = variant_id
        self.product_id = product_id
        self.name = name
        self.cost = cost
        self.price = price
        self.amazon_fee = amazon_fee
        self.fba_fee = fba_fee
        self.send_fee = send_fee
        self.profit = profit
        self.margin = margin
        # This is the row number of the line in excel
        self.row_id = str(row_id)

    def edit_product(self, cost, price, worksheet):
        ''' Change data on excel sheet for a product '''
        self.cost = cost
        self.price = price
        worksheet[COST_COL + self.row_id] = cost
        worksheet[PRICE_COL + self.row_id] = price
        return self

    def check_margin(self):
        ''' Check if the price margin is worth it '''
        if self.margin < .20:
            return MARGIN_TO_LOW
        else:
            return False
