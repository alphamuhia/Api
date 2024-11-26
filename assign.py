import requests
import csv

response = requests.get("https://fakestoreapi.com/products")

if response.status_code == 200:
    data = response.json()
    # print(len(data))

    with open('fakestore.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Category', 'Rating'])

        for products in data[9:10]:
            title = products["title"]
            price = products["price"]
            category = products["category"]
            rating = products["rating"]["rate"]


            writer.writerow([title, price, category, rating])
    print('products saves to fakestore.csv')
else:
    print('Faild to save products')