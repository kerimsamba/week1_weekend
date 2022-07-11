


customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

cc_pet_shop = {
            "pets": [
                {
                    "name": "Sir Percy",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "King Bagdemagus",
                    "pet_type": "cat",
                    "breed": "British Shorthair",
                    "price": 500
                },
                {
                    "name": "Sir Lancelot",
                    "pet_type": "dog",
                    "breed": "Pomsky",
                    "price": 1000,
                },
                {
                    "name": "Arthur",
                    "pet_type": "dog",
                    "breed": "Husky",
                    "price": 900,
                },
                {
                    "name": "Tristan",
                    "pet_type": "cat",
                    "breed": "Basset Hound",
                    "price": 800,
                },
                {
                    "name": "Merlin",
                    "pet_type": "cat",
                    "breed": "Egyptian Mau",
                    "price": 1500,
                }
            ],
            "admin": {
                "total_cash": 1000,
                "pets_sold": 0,
            },
            "name": "Camelot of Pets"
        }

pet_list = []
for pet in cc_pet_shop["pets"]:
    if pet["name"] == "Sir Percy":
        pet_list.append(pet["name"])
    #for next_level in cc_pet_shop[pet]:
     #   print(next_level)

print(pet_list)
print(len(pet_list))

name_of_pet = []
pet_name_to_find = "Arthur"
for each_pet in cc_pet_shop["pets"]:
    if each_pet["name"] == pet_name_to_find:
        name_of_pet.append(pet_name_to_find)
        #return each_pet["name"]
        print(each_pet["name"])

pet_name_to_find = "Arthur"
name_of_pet = {"name" : None}
for each_pet in cc_pet_shop["pets"]:
    if each_pet["name"] == pet_name_to_find:
        name_of_pet["name"] = pet_name_to_find
print(name_of_pet["name"])

for each_pet in cc_pet_shop["pets"]:
    if each_pet["name"] == pet_name_to_find:
        del each_pet


print("here")

print(customers[1]["cash"])
print(new_pet["price"])

if customers[1]["cash"] <= new_pet["price"]:
    print("ok")