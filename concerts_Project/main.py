from models import Band, Venue, Concert

def main():
    # Example usage
    Band.play_in_venue('Venue X', '2024-09-03')
    print(Band.all_introductions())
    print(Venue.concert_on('2024-09-01'))
    print(Venue.most_frequent_band())
    print(Band.most_performances())

if __name__ == "__main__":
    main()
