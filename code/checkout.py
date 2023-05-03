import sqlite3

def checkout(user_id):
    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # retrieve all items from the user's cart
    c.execute("SELECT * FROM carts WHERE user_id=?", (user_id,))
    cart_items = c.fetchall()

    # check if the user has any items in their cart
    if len(cart_items) == 0:
        print("Your shopping cart is empty.")
        return

    # loop through the items in the cart and update the stock information
    for cart_item in cart_items:
        # retrieve the item from the "items" table
        c.execute("SELECT * FROM items WHERE id=?", (cart_item[1],))
        item = c.fetchone()

        # check if there is enough stock to fulfill the order
        if item[3] < cart_item[3]:
            print(f"Sorry, there is not enough stock to fulfill your order of {cart_item[3]} {item[1]}")
            return
        else:
            # update the stock information in the "items" table
            new_stock = item[3] - cart_item[3]
            c.execute("UPDATE items SET stock=? WHERE id=?", (new_stock, item[0]))

    # create a new order in the "orders" table
    c.execute("INSERT INTO orders (user_id) VALUES (?)", (user_id,))
    order_id = c.lastrowid

    # add each item in the cart to the new order in the "order_items" table
    for cart_item in cart_items:
        c.execute("INSERT INTO order_items (order_id, item_id, quantity) VALUES (?, ?, ?)", (order_id, cart_item[1], cart_item[3]))

    # remove all items from the user's cart
    c.execute("DELETE FROM carts WHERE user_id=?", (user_id,))

    # commit the changes and close the database connection
    conn.commit()
    conn.close()

    print("Your order has been placed successfully!")
