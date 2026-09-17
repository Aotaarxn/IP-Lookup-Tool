import requests

ip = input("Enter the IP address:")
url = f"http://ipwho.is/{ip}"

response = requests.get(url)
print(response.status_code)

data = response.json()
print(f"IP Address: {data['ip']} \n Country: {data['country']} \n City: {data['city']} \n ISP: {data['connection']['isp']} \n Latitude: {data['latitude']} \n Longitude: {data['longitude']}")