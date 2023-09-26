import requests
url='https://maps.googleapis.com/maps/api/directions/json?destination=Montreal&origin=Toronto&key=AIzaSyDdtVDthhSWXzNCzORpZEVm6dc1K6-ZYCY'

out=requests.get(url)
print(dict(out.json()).keys())
