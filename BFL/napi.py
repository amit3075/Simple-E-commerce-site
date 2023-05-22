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