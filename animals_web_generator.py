import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    animal_type = animal.get("characteristics", {}).get("type")

    if name:
        print("Name:", name)

    if diet:
        print("Diet:", diet)

    if locations:
        print("Location:", locations[0])

    if animal_type:
        print("Type:", animal_type)

    print()