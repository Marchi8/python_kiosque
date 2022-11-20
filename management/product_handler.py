from collections import Counter
from menu import products


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    new_list = []
    for product in products:
        if product["type"] == type:
            new_list.append(dict(product.items()))
    return new_list


def menu_report():
    price_count = 0
    for product in products:
        price_count += product["price"]
        average = round(price_count, 2) / len(products)
        type_count = Counter(product["type"] for product in products)
        most_common_type = type_count.most_common(1)[0][0]
    return f"Products Count: {len(products)} - Average Price: ${round(average, 2)} - Most Common Type: {most_common_type}"


def add_product(products, **new_product):
    if len(products) == 0:
        new_id = 1
    else:
        new_id = max([product["_id"] for product in products]) + 1
    product_items = list(new_product.items())
    product_items.insert(0, ("_id", new_id))
    new_product = dict(product_items)
    products.append(new_product)
    return new_product


def add_product_extra(products, *required_keys, **new_product):
    for key in required_keys:
        if key not in new_product.keys():
            raise KeyError(f"field {key} is required")
    if len(products) == 0:
        new_id = 1
    new_id = max([product["_id"] for product in products]) + 1
    product_items = list(new_product.items())
    product_items.insert(0, ("_id", new_id))
    new_product = dict(product_items)
    products.append(new_product)
    return new_product
