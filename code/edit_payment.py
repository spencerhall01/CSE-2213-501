import sqlite3

def edit_payment(user_id, new_payment_info):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Update the user's payment information
    c.execute('UPDATE users SET payment_info = ? WHERE user_id = ?', (new_payment_info, user_id))
    conn.commit()

    # Close the connection to the database
    conn.close()

    print(f'User {user_id} payment information updated.')
