import sqlite3

def create_tables():
    conn = sqlite3.connect('store.db')
    c = conn.cursor()

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL UNIQUE,
                  password TEXT NOT NULL,
                  email TEXT NOT NULL UNIQUE,
                  shipping_address TEXT,
                  payment_info TEXT)''')

    # Create categories table
    c.execute('''CREATE TABLE IF NOT EXISTS categories
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL UNIQUE)''')

    # Create items table
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  price REAL NOT NULL,
                  stock INTEGER NOT NULL,
                  category_id INTEGER NOT NULL,
                  FOREIGN KEY (category_id) REFERENCES categories(id))''')

    # Create carts table
    c.execute('''CREATE TABLE IF NOT EXISTS carts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL UNIQUE,
                  FOREIGN KEY (user_id) REFERENCES users(id))''')

    # Create cart_items table
    c.execute('''CREATE TABLE IF NOT EXISTS cart_items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  cart_id INTEGER NOT NULL,
                  item_id INTEGER NOT NULL,
                  quantity INTEGER NOT NULL,
                  FOREIGN KEY (cart_id) REFERENCES carts(id),
                  FOREIGN KEY (item_id) REFERENCES items(id))''')

    # Create orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL,
                  total REAL NOT NULL,
                  date TEXT NOT NULL,
                  shipping_info TEXT,
                  payment_info TEXT,
                  FOREIGN KEY (user_id) REFERENCES users(id))''')

    # Create order_items table
    c.execute('''CREATE TABLE IF NOT EXISTS order_items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  order_id INTEGER NOT NULL,
                  item_id INTEGER NOT NULL,
                  quantity INTEGER NOT NULL,
                  FOREIGN KEY (order_id) REFERENCES orders(id),
                  FOREIGN KEY (item_id) REFERENCES items(id))''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    print("Tables created successfully")
