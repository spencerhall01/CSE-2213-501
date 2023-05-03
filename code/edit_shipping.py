import sqlite3

def edit_shipping(user_id, new_shipping_info):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Update the user's shipping information
    c.execute('UPDATE users SET shipping_info = ? WHERE user_id = ?', (new_shipping_info, user_id))
    conn.commit()

    # Close the connection to the database
    conn.close()

    print(f'User {user_id} shipping information updated.')
