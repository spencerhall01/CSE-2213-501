import sqlite3

def login():
    # get username and password from user input
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # check if username and password match a record in the database
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        print(f"Welcome, {username}!")
        # return the user's ID, which can be used to retrieve their data later
        return user[0]
    else:
        print("Invalid username or password.")
        return None

    # close the database connection
    conn.close()
