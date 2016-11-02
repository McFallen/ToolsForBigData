import sqlite3

db = sqlite3.connect("northwind.db")
db.text_factory = str
conn = db.cursor()
conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

print conn.fetchall()

#Exercise 5.2
# Create the dictionary to contain the order data
def get_orders_sql(customer):
    order_dict = {}
    conn.execute(""
                 "SELECT Orders.OrderID, Products.ProductID, Products.ProductName "
                 "FROM 'Order Details' "
                 "JOIN Orders "
                 "ON Orders.OrderID='Order Details'.OrderID "
                 "JOIN Products "
                 "ON Products.ProductID='Order Details'.ProductID "
                 "WHERE Orders.CustomerID=?", (customer,))

    for entry in conn.fetchall():
        if entry[0] in order_dict:
            order_dict[entry[0]].append((entry[2], entry[1]))
        else:
            order_dict[entry[0]] = [(entry[2], entry[1])]

    return order_dict

print "Exercise 5.2", get_orders_sql('ALFKI')

#Exercise 5.3
def get_order_with_x_or_more(x_amount, customer):
    # Container for which keys to remove
    ids_2_pop = []
    # All the order with products, belonging to ALFKI
    orders = get_orders_sql(customer)

    #Iterate over order-IDs
    for order_id in orders.iterkeys():

        # set() converts the list to a set - it has unique keys,
        # we just take the length of it and compares it to the given x_amount
        if len((orders[order_id])) < x_amount:
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
    uncle_ID = 7
    # Dict containing who => how many
    tears = {}

    # Fetches the name, ID and amount of pears, of each company, that has made an order for the pears
    orders = conn.execute("SELECT c.CompanyName, c.CustomerID, od.Quantity "
                          "FROM 'Order Details' od "
                          "JOIN Orders o ON o.OrderID=od.OrderID "
                          "JOIN Customers c ON c.CustomerID=o.CustomerID "
                          "WHERE od.ProductID=? ", (uncle_ID,))

    # Parse result
    for order in orders:
        if order[0] in tears:
            tears[order[0]] += order[2]
        else:
            tears[order[0]] = order[2]

    # return how many that ordered the pears and who
    return len(tears), tears

print "Exercise 5.4", uncle_bobs_dried_tears()

# Exercise 5.5
def uncle_bobs_associates():
    uncle_ID = 7
    # Dict containing who => how many
    asso = {}

    orders = conn.execute("SELECT p.ProductID, p.ProductName "
                          "FROM 'Order Details' o1 "
                          "JOIN 'Order Details' o2 on o1.OrderID=o2.OrderID "
                          "JOIN Products p on o2.ProductID=p.ProductID "
                          "WHERE o1.ProductID=? AND o2.ProductID!=o1.ProductID", (uncle_ID,))

    for order in orders.fetchall():
            asso[order[0]] = order[1]

    # return how many that ordered the pears and who
    return len(asso), asso

print "Exercise 5.5", uncle_bobs_associates()
