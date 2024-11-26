import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    # print(len(data))

    # for post in data[:5]:
    #     print(post)

# # create new 

new_post = {
    "userId": 10,
    "title": "New post",
    "body": "this is a new post"
}

response = requests.post(url, json=new_post)

if response.status_code == 201:
    post = response.json()
    print(post)
else:
    print("post creating faild")



# update_post ={
#     "userId": 1,
#     "title": "updated post",
#     "body": "This is the updated post"
# }

# id = 1

# response = requests.put(f"{url}/{id}", json=update_post)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Faild to update")

# response = requests.delete(f"{url}/{id}")

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to delete")
