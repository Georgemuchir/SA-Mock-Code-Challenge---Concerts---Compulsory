import sqlite3

def insert_test_data():
    conn = sqlite3.connect('concerts.db')
    c = conn.cursor()

    # Insert bands
    c.execute('''INSERT INTO bands (name, hometown) VALUES (?, ?)''', ('Band A', 'Hometown A'))
    c.execute('''INSERT INTO bands (name, hometown) VALUES (?, ?)''', ('Band B', 'Hometown B'))

    # Insert venues
    c.execute('''INSERT INTO venues (title, city) VALUES (?, ?)''', ('Venue X', 'City X'))
    c.execute('''INSERT INTO venues (title, city) VALUES (?, ?)''', ('Venue Y', 'City Y'))

    # Insert concerts
    c.execute('''INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)''', ('Band A', 'Venue X', '2024-09-01'))
    c.execute('''INSERT INTO concerts (band_name, venue_title, date) VALUES (?, ?, ?)''', ('Band B', 'Venue Y', '2024-09-02'))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_test_data()
