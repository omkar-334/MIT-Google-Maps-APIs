import requests
url = "https://ipgeolocation.abstractapi.com/v1"
querystring = {"api_key":"79d499d28ccd4bdca53185db9822e5cb","ip_address":"2409:4070:2d39:7f22::39ca:db0d","fields":"city,isp_name"}
response = requests.request("GET", url, params=querystring)
print(response.text)