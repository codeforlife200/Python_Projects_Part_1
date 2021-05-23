# import packages 
# pip install requests
import requests

# getting the http get request to api
res = requests.get('https://ipinfo.io/')
# getting the data from response
data = res.json()
# extracting the city from data 
city = data['city']
# extracting the lattitude and longitude from data
location = data['loc'].split(',')
lat = location[0]
long = location[1]


print('City : '+city)
print('lat, long : '+lat+' , '+long)
