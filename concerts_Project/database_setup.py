import sqlite3

def setup_database():
    conn = sqlite3.connect('concerts.db')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS bands (
                    name TEXT PRIMARY KEY,
                    hometown TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS venues (
                    title TEXT PRIMARY KEY,
                    city TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS concerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    band_name TEXT,
                    venue_title TEXT,
                    date TEXT,
                    FOREIGN KEY (band_name) REFERENCES bands(name),
                    FOREIGN KEY (venue_title) REFERENCES venues(title))''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
