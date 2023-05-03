import sqlite3

def remove_from_cart(item_id, user_id):
    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # retrieve the item from the user's cart
    c.execute("SELECT * FROM carts WHERE item_id=? AND user_id=?", (item_id, user_id))
    cart_item = c.fetchone()

    # check if the item is in the user's cart
    if cart_item is None:
        print("Sorry, that item is not in your cart.")
        return

    # retrieve the item from the "items" table
    c.execute("SELECT * FROM items WHERE id=?", (item_id,))
    item = c.fetchone()

    # update the item's stock
    new_stock = item[4] + cart_item[3]
    c.execute("UPDATE items SET stock=? WHERE id=?", (new_stock, item_id))
    conn.commit()

    # remove the item from the user's cart
    c.execute("DELETE FROM carts WHERE item_id=? AND user_id=?", (item_id, user_id))
    conn.commit()

    # close the database connection
    conn.close()

    print("Item removed from cart successfully!")
    