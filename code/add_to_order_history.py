import sqlite3

def add_order(user_id, item_id, quantity):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Add the order to the user's order history in the orders table
    c.execute('INSERT INTO orders (user_id, item_id, quantity) VALUES (?, ?, ?)', (user_id, item_id, quantity))

    # Commit the changes to the database
    conn.commit()

    # Print a message indicating that the order was added successfully
    print(f'Order added to user {user_id}\'s order history: item_id={item_id}, quantity={quantity}')

    # Close the connection to the database
    conn.close()
