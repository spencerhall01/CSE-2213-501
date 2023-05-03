import sqlite3

def view_cart(user_id):
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

    # print a header for the cart items
    print("Item ID  |  Item Name  |  Price  |  Quantity")
    print("-------------------------------------------")

    # loop through the items in the cart and print them
    for cart_item in cart_items:
        # retrieve the item from the "items" table
        c.execute("SELECT * FROM items WHERE id=?", (cart_item[1],))
        item = c.fetchone()

        # print the item's details
        print(f"{item[0]:<8} | {item[1]:<11} | ${item[2]:<6.2f} | {cart_item[3]:<8}")

    # close the database connection
    conn.close()
