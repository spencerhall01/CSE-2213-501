import sqlite3

def delete_account(user_id):
    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # delete the user's order history
    c.execute("DELETE FROM orders WHERE user_id=?", (user_id,))

    # delete the user's shopping cart
    c.execute("DELETE FROM cart_items WHERE user_id=?", (user_id,))

    # delete the user's account
    c.execute("DELETE FROM users WHERE id=?", (user_id,))

    # commit changes to the database
    conn.commit()

    # close the database connection
    conn.close()

    print("Account and associated data deleted successfully.")
