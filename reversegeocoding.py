import googlemaps as gm
key=open('key.txt','r').read()
client = gm.Client(key)

def reverse_geocode(client, latlng, result_type=None, location_type=None,
                    language=None):
    """
    Reverse geocoding is the process of converting geographic coordinates into a
    human-readable address.

    :param latlng: The latitude/longitude value or place_id for which you wish
        to obtain the closest, human-readable address.
    :type latlng: string, dict, list, or tuple

    :param result_type: One or more address types to restrict results to.
    :type result_type: string or list of strings

    :param location_type: One or more location types to restrict results to.
    :type location_type: list of strings

    :param language: The language in which to return results.
    :type language: string

    :rtype: list of reverse geocoding results.
    """

    # Check if latlng param is a place_id string.
    #  place_id strings do not contain commas; latlng strings do.
    if gm.convert.is_string(latlng) and ',' not in latlng:
        params = {"place_id": latlng}
    else:
        params = {"latlng": gm.convert.latlng(latlng)}

    if result_type:
        params["result_type"] = gm.convert.join_list("|", result_type)

    if location_type:
        params["location_type"] = gm.convert.join_list("|", location_type)

    if language:
        params["language"] = language

    return client._request("/maps/api/geocode/json", params)
#.get("results", [])
out=reverse_geocode(client,latlng=(-33.8674869, 151.2069902))
print(out)