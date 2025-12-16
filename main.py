from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Product(id=1, name="Laptop", description="lenovo", price=1200, quantity=10), 
    Product(id=2, name="Smartphone",description="iphone", price=800, quantity=20),
    Product(id=3, name="Webcam", description="birro", price=120, quantity=4), 
    Product(id=4, name="Converter",description="usb", price=80, quantity=12)
]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated"
    return {"error": "Product not found"}

@app.delete("/products")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "message" "Product deleted"
    return {"error": "Product not found"}
