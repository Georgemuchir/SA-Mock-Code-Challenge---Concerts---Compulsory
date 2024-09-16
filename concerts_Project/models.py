import sqlite3

class Band:
    @staticmethod
    def concerts():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM concerts WHERE band_name = ?''', (Band.name,))
        results = c.fetchall()
        conn.close()
        return results

    @staticmethod
    def venues():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT venues.* FROM venues
                     JOIN concerts ON venues.title = concerts.venue_title
                     WHERE concerts.band_name = ?''', (Band.name,))
        results = c.fetchall()
        conn.close()
        return results

    @staticmethod
    def play_in_venue(venue_title, date):
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''INSERT INTO concerts (band_name, venue_title, date)
                     VALUES (?, ?, ?)''', (Band.name, venue_title, date))
        conn.commit()
        conn.close()

    @staticmethod
    def all_introductions():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT DISTINCT venues.city FROM concerts
                     JOIN venues ON concerts.venue_title = venues.title
                     WHERE concerts.band_name = ?''', (Band.name,))
        cities = c.fetchall()
        introductions = []
        for city in cities:
            introductions.append(f"Hello {city[0]}!!!!! We are {Band.name} and we're from {Band.hometown}")
        conn.close()
        return introductions

    @staticmethod
    def most_performances():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT band_name FROM concerts
                     GROUP BY band_name
                     ORDER BY COUNT(*) DESC
                     LIMIT 1''')
        result = c.fetchone()
        conn.close()
        return result[0]

class Venue:
    @staticmethod
    def concerts():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM concerts WHERE venue_title = ?''', (Venue.title,))
        results = c.fetchall()
        conn.close()
        return results

    @staticmethod
    def bands():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT DISTINCT bands.* FROM bands
                     JOIN concerts ON bands.name = concerts.band_name
                     WHERE concerts.venue_title = ?''', (Venue.title,))
        results = c.fetchall()
        conn.close()
        return results

    @staticmethod
    def concert_on(date):
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM concerts
                     WHERE venue_title = ? AND date = ?
                     LIMIT 1''', (Venue.title, date))
        result = c.fetchone()
        conn.close()
        return result

    @staticmethod
    def most_frequent_band():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT band_name FROM concerts
                     WHERE venue_title = ?
                     GROUP BY band_name
                     ORDER BY COUNT(*) DESC
                     LIMIT 1''', (Venue.title,))
        result = c.fetchone()
        conn.close()
        return result[0]

class Concert:
    @staticmethod
    def band():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM bands
                     JOIN concerts ON bands.name = concerts.band_name
                     WHERE concerts.id = ?''', (Concert.id,))
        result = c.fetchone()
        conn.close()
        return result

    @staticmethod
    def venue():
        conn = sqlite3.connect('concerts.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM venues
                     JOIN concerts ON venues.title = concerts.venue_title
                     WHERE concerts.id = ?''', (Concert.id,))
        result = c.fetchone()
        conn.close()
        return result

    @staticmethod
    def hometown_show():
        band = Concert.band()
        venue = Concert.venue()
        return band['hometown'] == venue['city']

    @staticmethod
    def introduction():
        band = Concert.band()
        venue = Concert.venue()
        return f"Hello {venue['city']}!!!!! We are {band['name']} and we're from {band['hometown']}"
