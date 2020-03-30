import sys
sys.path.insert(0, '/Users/TimmyC/Desktop/astral-grow-shopify-api')

from secrets.secrets import (
    API_KEY,
    API_PASSWORD,
    SHOP_NAME,
    API_VERSION,
)

import shopify
import xlrd

shop_url = "https://%s:%s%s%s" % (API_KEY, API_PASSWORD, SHOP_NAME, API_VERSION)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()
test_id = 2182140952687
variant_id = 20465563205743
# This is used to find the cost from inventory item
inventory_id = 20863332778095


def get_inventory_item(inventory_item_id):
    return shopify.InventoryItem.find(inventory_item_id)


def get_product_details(product_id, variant_id=None):
    ''' Grab product details from shopify REST API '''

    # First grab the product using product_id
    product = shopify.Product.find(product_id)
    variants = product.variants
    matched_product = None

    # Check variants and grab the inventory_item if it exists to get costs
    if variants and len(variants) == 1:
        matched_product = variants[0]
        inventory_item = get_inventory_item(matched_product.inventory_item_id)
    elif variants and len(variants) > 1:
        for variant in product.variants:
            if variant_id and variant_id == variant.id:
                matched_product = variant
                inventory_item = get_inventory_item(variant.inventory_item_id)
    else:
        return "Product doesn't exist"

    product_details = {
            'Product Name': product.title,
            'Product Price': matched_product.price,
            'Product Cost': inventory_item.cost,
        }

    return product_details

# Need to figure out how to authorize access for Graphql
# def get_product_graphql(variant_id):
#     client = shopify.GraphQL()
#     query = '''
#         {
#             product(id: "gid://shopify/Product/%s" % (test_id)) {
#                 id
#                 handle
#                 variants (first:1) {
#                     edges {
#                         node {
#                             title
#                         }
#                     }
#                 }
#             }
#         }
#     '''
#     result = client.execute(query)
#     return result

details = get_product_details(test_id, variant_id)
print(details)

