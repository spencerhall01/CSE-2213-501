import sqlite3

def view_order_history(user_id):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Query the database for the user's order history
    c.execute('SELECT * FROM orders WHERE user_id = ?', (user_id,))
    orders = c.fetchall()

    # Print the user's order history
    if orders:
        print(f'Order history for user {user_id}:')
        for order in orders:
            print(f' - item_id={order[2]}, quantity={order[3]}')
    else:
        print(f'User {user_id} has no order history.')

    # Close the connection to the database
    conn.close()
