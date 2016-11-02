from pymongo import MongoClient

mc = MongoClient("localhost", 27017)
db = mc["Northwind"]

# Exercixe 5.1
print db.collection_names()

#Exercise 5.2
# Create the dictionary to contain the order data
def get_order_mongo(customer):
    order_dict = {}

    # Initialize the products, so we don't have to do that every single time we want to lookup a product.
    products = db.get_collection('products')

    # Iterate over all the orders that belongs to the customer with ID ALFKI
    for order in db.get_collection('orders').find({'CustomerID': customer}):
        # Init array in the dictionary for the evaluated order
        order_dict[order['OrderID']] = []
        # Iterate over all the order details with evaluated order-ID
        for details in db.get_collection('order-details').find({'OrderID': order['OrderID']}):
            # Append the product-ID to the list of ordered products within the dictionary
            order_dict[details['OrderID']].append(products.find_one({'ProductID': details['ProductID']})['ProductName'])
        order_dict[order['OrderID']] = set(order_dict[order['OrderID']])

    return order_dict

print "Exercise 5.2", get_order_mongo('ALFKI')

#Exercise 5.3
def get_order_with_x_or_more(x_amount, costumer):
    # Container for which keys to remove
    ids_2_pop = []
    # All the order with products, belonging to ALFKI
    orders = get_order_mongo(costumer)

    #Iterate over order-IDs
    for order_id in orders.iterkeys():

        # set() converts the list to a set - it has unique keys,
        # we just take the length of it and compares it to the given x_amount
        if len(orders[order_id]) < x_amount:
            # Add ID to be popped if it has under x_amount of different products
            ids_2_pop.append(order_id)
    # Popping loop
    for id in ids_2_pop:
        orders.pop(id)

    # orders containing x_amount or more different product types
    return orders

print "Exercise 5.3", get_order_with_x_or_more(2, 'ALFKI')


# Exercise 5.4
def uncle_bobs_dried_tears():

    # Dict containing who => how many
    tears = {}

    # Select all order-details containing the product-ID for the pears
    for order_details in db.get_collection('order-details').find({'ProductID': 7}):
        # Fetch order for the given order-ID
        order = db.get_collection('orders').find_one({'OrderID': order_details['OrderID']})
        # Fetch customer for the given customer-ID
        customer = db.get_collection('customers').find_one({'CustomerID': order['CustomerID']})

        # Insert / update customer, using the name of the company as key for the dictionary
        if customer['CompanyName'] in tears:
            tears[customer['CompanyName']] += order_details['Quantity']
        else:
            tears[customer['CompanyName']] = order_details['Quantity']

    # return how many that ordered the pears and who
    return len(tears), tears

print "Exercise 5.4", uncle_bobs_dried_tears()

# Exercise 5.5
def uncle_bobs_associates():
    uncle_bob_id = 7
    # Get products for future look-ups
    products = db.get_collection('products')

    # Get order-details for future look-ups
    order_details = db.get_collection('order-details')

    # Associates of uncle bob
    associates = []

    # Fetch all order-ID where uncle bob is in
    # Select all order-details containing the product-ID for the pears
    for order_detail in order_details.find({'ProductID': 7}):
        # Fetch other order-details for the given order-ID and iterate through them
        for product in order_details.find({'OrderID': order_detail['OrderID']}):
            # Fetch product info for the given customer-ID
            product = products.find_one({'ProductID': product['ProductID']})

            associates.append(product['ProductName'])

    associates_uniq = set(associates)
    associates_uniq.remove("Uncle Bob's Organic Dried Pears")
    # returns how many different- and which products
    return len(associates_uniq), associates_uniq

print "Exercise 5.5", uncle_bobs_associates()
