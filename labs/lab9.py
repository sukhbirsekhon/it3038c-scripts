import json 
import requests 

# Call locolhost API running on node server
r = requests.get('http://localhost:3000') 
data=r.json() 

# Format the data 
for d in range(len(data)):
    print('%s is %s.' % (data[d]['name'], data[d]['color']))