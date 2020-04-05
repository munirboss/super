i = 1
while i <= 5:
    print(i)
    i = i + 1
print("hello world")

num = ["hello", "world", "love", "it", "here"]
for no in num:
    print(no + ",")

def my_func():
    print("hello") 
    print("my name is")  
    print("munir")
my_func()


nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]): 
    print("all larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")  

for v in enumerate(nums):
    print(v)


class Phone:
    brand = "munirboss"
    price = "20000"

my_phone = Phone
print(my_phone.brand)   
print(my_phone.price)

class Calculator:
     brand = "Texas Instruments"
     def deduct (self,a, b):
         return a - b
my_calc = Calculator()
result = my_calc.deduct(15,8)
print(result)   

class Shopping:
    def __init__(self):
        self.cart = []
    def add_to_cart(self, item):
        self.cart.append(item)  
customer1 = Shopping()
customer1.add_to_cart('t-shirt')
print(customer1.cart)  

customer2 = Shopping()
customer2.add_to_cart('shoes')
print(customer2.cart)

class Watch():
    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.steps_count = 0
        self.has_gps = has_gps
    def recharge(self):
          print('Eating Electricity')
          print('Electrons are Yummy!')

my_watch = Watch('Fitbit',200,False)
my_watch.recharge()   

numb = input('')
print(numb + ' pika')

p = 0
while p <= 10:
    print(p)
    p = p + 1

lin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
for l in lin:
       print(l)
