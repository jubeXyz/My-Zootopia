import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

output = ""

for animal in animals_data:
    output += '<li class="cards__item">'
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations", [])
    animal_type = animal.get("characteristics", {}).get("type")

    if name:
        output += f"Name: {name}<br/>\n"

    if diet:
        output += f"Diet: {diet}<br/>\n"

    if locations:
        output += f"Location: {locations[0]}<br/>\n"

    if animal_type:
        output += f"Type: {animal_type}<br/>\n"

    output += "\n"
    output += "</li>\n"

with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html)