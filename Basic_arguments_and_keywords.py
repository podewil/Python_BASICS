def GPS_location(name = 'New York', Latitude ='40.7418', Longitude = '-73.9893'):
    print(name, Latitude, Longitude)


GPS_location()
GPS_location("Seoul", "37.5665", "126.9779")
GPS_location("Los Angeles", "Latitude", "Longitude")

updated_location1 = GPS_location(Latitude="0.0000")
GPS_location(Longitude='1.1111')

print(updated_location1)

'''
New York 40.7418 -73.9893
Seoul 37.5665 126.9779
Los Angeles Latitude Longitude
New York 0.0000 -73.9893
New York 40.7418 1.1111
'''