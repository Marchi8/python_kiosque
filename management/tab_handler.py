from menu import products


def calculate_tab(tables):
    subtotal = 0
    for table in tables:
        for product in products:
            if table["_id"] == product["_id"]:
                subtotal += table["amount"] * product["price"]
    return {"subtotal": f"${round(subtotal, 2)}"}
