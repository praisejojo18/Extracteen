from extraction.api_client import get_data

url = "https://dummyjson.com/products"

params ={
    "limt": 5,
    "skip": 10
}

data = get_data(url, params=params)
#print(data)

print("Total products:", data["total"])
print("Products returned:", len(data["products"]))