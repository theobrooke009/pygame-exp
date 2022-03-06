person = {
    "name": "jack",
    "age": 31
}

print(person)

print(person["name"])

person["age"] = 21

person["hometown"] = 'Portsmouth'

print(person)

pet_name = person.get('pet-name', 'Mac')

print(pet_name)
