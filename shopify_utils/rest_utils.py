# Functions to access shopify REST API

def get_inventory_item(shopify, inventory_item_id):
    return shopify.InventoryItem.find(inventory_item_id)


def get_product_details(shopify, product_id, variant_id=None):
    ''' Grab product details from shopify REST API '''

    # First grab the product using product_id
    product = shopify.Product.find(product_id)
    variants = product.variants
    matched_product = None

    # Check variants and grab the inventory_item if it exists to get costs
    if variants and len(variants) == 1:
        matched_product = variants[0]
        inventory_item = get_inventory_item(shopify, matched_product.inventory_item_id)
    elif variants and len(variants) > 1:
        for variant in product.variants:
            if variant_id and variant_id == variant.id:
                matched_product = variant
                inventory_item = get_inventory_item(shopify, variant.inventory_item_id)
    else:
        return "Product doesn't exist"

    product_details = {
            'Product Name': product.title,
            'Product Price': matched_product.price,
            'Product Cost': inventory_item.cost,
        }

    return product_details
