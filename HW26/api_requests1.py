import requests

headers = {"Content-Type": "application/json"}
data = {"id":101, "userId":8}

response = requests.get("https://jsonplaceholder.typicode.com/posts/80")
print(response.json())
response2 = requests.get("https://jsonplaceholder.typicode.com/comments?postId=60")
print(response2.json())
response3 = requests.post("https://jsonplaceholder.typicode.com/posts/", headers = headers, json = data)
print(response3.status_code)
print(response3.json())
response4 = requests.delete("https://jsonplaceholder.typicode.com/posts/7")
print(response4.status_code)
