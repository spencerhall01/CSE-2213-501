import sqlite3

def create_account():
    # get user information from user input
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")
    shipping_address = input("Enter your shipping address: ")
    payment_info = input("Enter your payment information: ")

    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # check if the username is already taken
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = c.fetchone()

    if existing_user:
        print("That username is already taken.")
    else:
        # insert new user into the database
        c.execute("INSERT INTO users (username, password, email, shipping_address, payment_info) VALUES (?, ?, ?, ?, ?)",
                  (username, password, email, shipping_address, payment_info))
        conn.commit()
        print("Account created successfully.")

    # close the database connection
    conn.close()
