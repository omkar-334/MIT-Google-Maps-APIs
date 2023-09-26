# Python program to get a google map
# image of specified location using
# Google Static Maps API

# importing required modules
import requests

# Enter your api key here
api_key ='AIzaSyDdtVDthhSWXzNCzORpZEVm6dc1K6-ZYCY'

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map,
# equidistant from all edges of the map.
center = "Dehradun"

# zoom defines the zoom
# level of the map
zoom = 10

# get method of requests module
# return response object
r =requests.get(url + "center=" + center + "&zoom=" +
				str(zoom) + "&size=400x400&key=" +
							api_key)
# wb mode is stand for write binary mode
f = open('map.jpg', 'wb')

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()
