from animal_class import Pet

pets = [
    {
        "animal": "кошка",
        "name": "Барон",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "animal": "кошка",
        "name": "Сэм",
        "gender": "мальчик",
        "age": 2,
    }
]

for num in pets:
    pet_obj = Pet()
    pet_obj.init_from_dict(num)

    print(f"\nВид: {pet_obj.animal}\nИмя: {pet_obj.name}"
          f"\nПол: {pet_obj.gender}\nВозраст: {pet_obj.age}")
