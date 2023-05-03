import sqlite3

def add_to_cart(item_id, user_id, quantity):
    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # retrieve the item from the database
    c.execute("SELECT * FROM items WHERE id=?", (item_id,))
    item = c.fetchone()

    # check if the item is in stock
    if item[4] < quantity:
        print("Sorry, we do not have enough stock for that item.")
        return

    # add the item to the user's shopping cart
    c.execute("INSERT INTO carts (user_id, item_id, quantity) VALUES (?, ?, ?)", (user_id, item_id, quantity))
    conn.commit()

    # update the item's stock
    new_stock = item[4] - quantity
    c.execute("UPDATE items SET stock=? WHERE id=?", (new_stock, item_id))
    conn.commit()

    # close the database connection
    conn.close()

    print("Item added to cart successfully!")
