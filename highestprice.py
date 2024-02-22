def find_highest_priced_product(products):
    highest_price = float("-inf") #to start off initial price as the lowest price
    highest_product_name = None     #to start with no product name

    for product in products:     #for loop to iterate tru each dictionary in the list
        product_name = str(product["name"]) #to extract names from each dictionary in the list
        product_price = float(product["price"])   #to extract prices from each dictionary in the list
        if product_price >= highest_price:  #>= to compare if the product price is higher or equal to the highest price
            highest_price = product_price     #replacing highest price with product price if condition true
            highest_product_name = product_name
    return highest_product_name #return name of product with highest price


products = [
    {"name":"gel nails", "price":"500.00"},
    {"name":"regular nails", "price":"250.00"},
    {"name":"nail repair","price":"300.00"},
    {"name":"french","price":"900.00"},
    {"name":"tip removal","price":"100.00"}
    ]
       
highest_product = find_highest_priced_product(products)
print(f"the product with highest price is : {highest_product}")


  


