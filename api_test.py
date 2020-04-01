import sys
sys.path.insert(0, '/Users/TimmyC/Desktop/astral-grow-shopify-api')

from excel_utils.excel_data import get_excel_sheet, make_store
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

details = get_product_details(shopify, test_id, variant_id)
print(details)

work_sheet = get_excel_sheet('excelsheets/test.xlsx', 'test')

store = make_store('Astral Grow', work_sheet)
print(store.products)
