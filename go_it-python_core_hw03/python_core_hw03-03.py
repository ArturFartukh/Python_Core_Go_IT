base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global base_rate
    global total_trip
    total_trip += 1
    return base_rate + path * 10
