# Need to figure out how to authorize access for Graphql


def get_product_graphql(variant_id, shopify):
    client = shopify.GraphQL()
    query = '''
        {
            product(id: "gid://shopify/Product/%s" % (test_id)) {
                id
                handle
                variants (first:1) {
                    edges {
                        node {
                            title
                        }
                    }
                }
            }
        }
    '''
    result = client.execute(query)
    return result
