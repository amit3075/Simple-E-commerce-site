"""print(f"file one __name__ is set to :{__name__}")
import file2
print("file One __name__ is set to :{}".format(__name__))
import requests
resp = requests.get('https://www.google.com/search?q=amit')
print(resp.status_code)
print(resp.headers)
print(resp.content)
print(type(resp.content))

with open('serp.html','wb') as file:
    file.write(resp.content)
    file.close()
import requests
#api endpoint
URL ="https://reqres.in/api/users"
#location given here 
page =2
# defining get req and save 
PARAMS ={'page':page}
#sending get req and saving the responswe as response obj
r = requests.get(url=URL,params=PARAMS)
print(r.url)
print(r.json())
#passing headers 
headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Content-Type' :'text/html'}
r =requests.get('https:httpbin.org/basic-auth/user/pass',auth=('user','pass'))
print(r.content)
import requests
base = 'USD'
url =f"https://api.apilayer.com/fixer/lastest?base={base}"
payload ={}
headers ={
    "apikey: w2fiYnt2CuI5ARdBUmBUm1Y3QL7w7Kt1"
}
response = requests.get(url,headers = headers,params = payload)
status_code = response.status_code
result = response.json()
print(result)
import requests
url = "https://httpbin.org/post"
data ={
    "id": 200,
    "name":"SomeOne",
    "passion": "coding",
}
response = request.post(url,json =data)
print("status code ,response.status_code")
print(response.url)
print("JSON Response",response.json())

# count num of letter in word in pythonic way
from  collections import Counter
word = "ambitioon"
print(Count(word))
print(dict(Counter(word)))"""
import heapq
#initialzies
li =[12,33,44,4455,66]
heapq.heapify(li)
print("This created heap is :",end="")
print(list(li))
#using heappush() to push element into heap
heapq.heappush(li,4)
#print modify heap
print("the modify heap after push :",end ="")
print(list(li))
