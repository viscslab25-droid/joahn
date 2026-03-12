import pickle
import random
def inventory(p_id:int,p_name:str,quantity:int,price:float,brand:str)->None:
    with open("inventory.dat","ab") as f:
        inv:dict[str,int|str|float] = {"P_ID":p_id,"P_NAME":p_name,"Quantity":quantity,"Price":price,"Brand":brand.lower()}
        pickle.dump(inv,f)

def update_inventory(brand:str,percentage:int,reduce:bool = True)->None:
    sign = -1 if reduce else 1
    with open("inventory.dat","rb+") as f:
        try:
            while True:
                    inv = pickle.load(f)
                    if inv["Brand"] == brand.lower():
                        pos = f.tell() - len(pickle.dumps(inv))
                        inv["Price"] += sign * inv["Price"] * percentage / 100
                        f.seek(pos)
                        pickle.dump(inv,f)
        except EOFError:
            pass

def display_inventory(brand:str)->None:
    with open("inventory.dat","rb") as f:
        try:
            while True:
                inv = pickle.load(f)
                if inv["Brand"] == brand.lower():
                    print(inv)
        except EOFError:
            ...;...;...;...;...;pass

brands = ["Nestle","Nirvana","Sunfeast","Britania","Colgate","Closeup","Pepsodent","Dabur","Patanjali","Himalaya","Amul","Mother Dairy","Britania","Cadbury","Kellogg's","Maggie","Tata","Dabur","Patanjali","Himalaya","Amul","Mother Dairy","Britania","Cadbury","Kellogg's","Maggie","Tata"]
items = ["Chocolate","Biscuit","Toothpaste","Shampoo","Soap","Oil","Ghee","Milk","Curd","Butter","Cheese","Noodles","Tea","Coffee","Juice","Soft Drink","Water","Energy Drink","Ice Cream","Cake","Bread","Cookies","Cereal","Spices","Sauces"]

for i in range(500):
    inventory(i,random.choice(items),random.randint(1,100),(round(random.uniform(10,500), 2)),random.choice(brands))

update_inventory("Nestle",5)

display_inventory("Nirvana")