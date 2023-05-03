import sqlite3

def search(category):
    # connect to the database
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # retrieve items from the database for the given category
    c.execute("SELECT * FROM items WHERE category=?", (category,))
    items = c.fetchall()

    # display the items
    if len(items) == 0:
        print("No items found in this category.")
    else:
        for item in items:
            print("Name:", item[1])
            print("Description:", item[2])
            print("Price:", item[3])
            print("Stock:", item[4])
            print("Category:", item[5])
            print("----------------------")

    # close the database connection
    conn.close()
