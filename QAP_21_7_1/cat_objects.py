from cat_class import Cat

cats = [
    {
        "name": "Барон",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "name": "Сэм",
        "gender": "мальчик",
        "age": 2,
    }
]

for num in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(num)

    print(f"\nВид: кошка\nИмя: {cat_obj.name}"
          f"\nПол: {cat_obj.gender}\nВозраст: {cat_obj.age}")

