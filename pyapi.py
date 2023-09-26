import googlemaps
import gmaps
from datetime import datetime
key=open('key.txt','r').read()
gm = googlemaps.Client(key=key)
# gmaps.configure(api_key=key)
# new_york_coordinates = (40.75, -74.00)
# out=gmaps.figure(center=new_york_coordinates, zoom_level=12)


# # Geocoding an address
geocode_result = gm.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gm.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gm.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gm.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

print(directions_result)