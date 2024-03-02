class OnlineStore:
    def __init__(self):
        self.cart=[]
    
    def add_to_cart(self,product,quantity):
        self.cart.append((product,quantity))
    
    def calculate(self):
        total_price=0
        for product,quntity in self.cart:
            total_price+=product.price*quntity
        return total_price
    
    def checkout(self):
        total_price=self.calculate()
        print(f"total price:{total_price}")
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price


p1=Product("laptap",1400)
p2=Product("mobile",700)

store=OnlineStore()
store.add_to_cart(p1,2)
store.add_to_cart(p2,1)

total_price=store.calculate()
print("total is:",total_price)
store.checkout()
