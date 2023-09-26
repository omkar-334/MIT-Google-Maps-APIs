import googlemaps as gm

key=open('key.txt','r').read()
client = gm.Client(key)
address=input("Enter Address - ")
# components={"country":input("Enter Country - ")}

def geocode(client, address=None, place_id=None, components=None, bounds=None, region=None,
            language=None):
    params = {}
    if address:
        params["address"] = address
    if place_id:
        params["place_id"] = place_id
    if components:
        params["components"] = gm.convert.components(components)
    if bounds:
        params["bounds"] = gm.convert.bounds(bounds)
    if region:
        params["region"] = region
    if language:
        params["language"] = language
    return client._request("/maps/api/geocode/json", params)
# .get("results", [])

js=geocode(client,address=address)

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat :', lat, ', lng: ', lng)
location = js['results'][0]['formatted_address']
print(location)
