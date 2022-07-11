# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, amount):
    cc_pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, number_of_pets_sold):
   cc_pet_shop["admin"]["pets_sold"] += number_of_pets_sold


def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, selected_breed):
    list_of_breeds = []
    
    for each_pet in cc_pet_shop["pets"]:
        if each_pet["breed"] == selected_breed:
            list_of_breeds.append(selected_breed)
    return list_of_breeds

def find_pet_by_name(cc_pet_shop, pet_name_to_find):
    name_of_pet = {"name" : None}
    for each_pet in cc_pet_shop["pets"]:
        if each_pet["name"] == pet_name_to_find:
            name_of_pet["name"] = pet_name_to_find
            return name_of_pet
    return name_of_pet["name"]

def remove_pet_by_name(cc_pet_shop, pet_name_to_find):
    counter = 0
    for each_pet in cc_pet_shop["pets"]:
        if each_pet["name"] == pet_name_to_find:
            del cc_pet_shop["pets"][counter]
        counter += 1
        
def add_pet_to_stock(cc_pet_shop, pet_to_add):
    cc_pet_shop["pets"].append(pet_to_add)

def get_customer_cash(customer_number):
    return customer_number["cash"]

def remove_customer_cash(customer_number, cash_to_removed):
    customer_number["cash"] -= cash_to_removed

def get_customer_pet_count(customer_number):
    return len(customer_number["pets"])

def add_pet_to_customer(customer_number, pet_to_add):
    customer_number["pets"].append(pet_to_add)

def customer_can_afford_pet(customer_number, planned_purchase):
    if customer_number["cash"] >= planned_purchase["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(cc_pet_shop, pet_sold, customer):
    cc_pet_shop["admin"]["total_cash"] += pet_sold["price"]
    customer["cash"] -= pet_sold["price"]
    customer["pets"].append(pet_sold)
    remove_pet_by_name[cc_pet_shop, pet_sold]
    increase_pets_sold(cc_pet_shop, 1)
    remove_pet_by_name(cc_pet_shop, pet_sold)

   

