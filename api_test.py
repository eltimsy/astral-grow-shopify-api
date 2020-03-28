import sys
sys.path.insert(0, '/Users/TimmyC/Desktop/astral-grow-shopify-api')

from secrets.secrets import (
    API_KEY,
    API_PASSWORD,
    SHOP_NAME,
    API_VERSION,
)

import shopify

shop_url = "https://%s:%s%s%s" % (API_KEY, API_PASSWORD, SHOP_NAME, API_VERSION)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()

product = shopify.Product.find(2182140952687)

print(product.title)
