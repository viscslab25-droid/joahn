import pickle
def inventory(p_id:int,p_name:str,quantity:int,price:float,brand:str)->None:
    with open("inventory.dat","ab") as f:
        inv:dict[str,int|str|float] = {"P_ID":p_id,"P_NAME":p_name,"Quantity":quantity,"Price":price,"Brand":brand}
        pickle.dump(inv,f)

def update_inventory(percentage:int,reduce:bool = True)->None:
    ...