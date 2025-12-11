
import json

def generate_card_content(animal):
    name = animal.get('name', 'N/A')
    card_html = f"""
            <li class="cards__item">
                <div class="card__title">{name}</div>
                <div class="card__text">
    """
    # Characteristics
    characteristics = animal.get('characteristics', {})
    card_html += " <strong>Characteristics:</strong> <br>"
    for key, value in characteristics.items():
        display_key = key.replace('_', ' ').title()
        display_value = ", ".join(value) if isinstance(value, list) else value
        if display_value and display_value != 'N/A' and display_key not in ['Common Name', 'Slogan', 'Type', 'Group']:
            card_html += f"<strong>{display_key}:</strong> {display_value}<br>"
    # Locations
    locations = animal.get('locations', [])
    if locations:
        card_html += f" <strong>Locations:</strong> {', '.join(locations)}<br>"
    # Taxonomy
    taxonomy = animal.get('taxonomy', {})
    card_html += " <strong>Taxonomy:</strong> <br>"
    for key, value in taxonomy.items():
        if value:
            display_key = key.replace('_', ' ').title()
            card_html += f"<strong>{display_key}:</strong> {value}<br>"
    # Slogan
    slogan = characteristics.get('slogan')
    if slogan:
        card_html += f"<br> <strong>Summary:</strong> *{slogan}*"
    card_html += """
                </div>
            </li>
    """
    return card_html

def generate_animal_website(data, template):
    all_cards_html = ""
    for animal in data:
        all_cards_html += generate_card_content(animal)
    return template.replace("__REPLACE_ANIMALS_INFO__", all_cards_html)

if __name__ == "__main__":
    # Lade JSON-Daten
    with open("animal_data.json", "r") as f:
        animal_data = json.load(f)

    # Lade HTML-Template
    with open("template.html", "r") as f:
        html_template = f.read()

    # Erzeuge finale HTML-Seite
    final_html = generate_animal_website(animal_data, html_template)

    # Schreibe in Datei
    with open("animal_repository.html", "w") as f:
        f.write(final_html)

    print("Website generated: animal_repository.html")
