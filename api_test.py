import sys
sys.path.insert(0, '/Users/TimmyC/Desktop/astral-grow-shopify-api') # noqa

from excel_utils.excel_data import get_excel_data, make_store
from secrets.secrets import (
    API_KEY,
    API_PASSWORD,
    SHOP_NAME,
    API_VERSION,
)
from shopify_utils.rest_utils import get_product_details

import shopify


shop_url = "https://%s:%s%s%s" % (API_KEY, API_PASSWORD, SHOP_NAME, API_VERSION)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()
test_id = 2182140952687
variant_id = 20465563205743
# This is used to find the cost from inventory item
inventory_id = 20863332778095
sheet_location = 'excelsheets/test.xlsx'

details = get_product_details(shopify, test_id, variant_id)
print(details)

wb, work_sheet = get_excel_data(sheet_location, 'test')

store = make_store('Astral Grow', work_sheet)
print(store.products)

updated_product = store.change_product('Test Light', 50, 100, work_sheet)
wb.save(filename=sheet_location)
print(updated_product.price)
