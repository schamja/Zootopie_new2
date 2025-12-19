import json


def generate_card_html(animal):
    """Generiert den HTML-Inhalt für ein Tier basierend auf den JSON-Daten."""
    name = animal.get('name')
    if not name:
        return ""

    card_content = f"Name: {name}\n"

    # Eigenschaften sicher extrahieren
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet')
    if diet:
        card_content += f"Diet: {diet}\n"

    locations = animal.get('locations')
    if locations and isinstance(locations, list):
        card_content += f"Location: {locations[0]}\n"

    animal_type = animal.get('type')
    if animal_type:
        card_content += f"Type: {animal_type}\n"

    # Rückgabe des HTML-Bausteins
    return f"""
            <li class="cards__item">
                <div class="card__title"></div>
                <div class="card__text">
{card_content}
                </div>
            </li>
    """


def main():
    # 1. Template laden (Pfad anpassen, falls die Datei in einem Unterordner liegt)
    try:
        with open("animals_template.html", "r", encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print("Fehler: 'animals_template.html' nicht gefunden. Stelle sicher, dass sie im selben Ordner liegt.")
        return

    # 2. JSON-Daten laden
    try:
        with open("animals_data.json", "r", encoding='utf-8') as f:
            animal_data = json.load(f)
    except FileNotFoundError:
        print("Fehler: 'animals_data.json' nicht gefunden.")
        return

    # 3. HTML für alle Karten generieren
    all_cards_html = ""
    for animal in animal_data:
        all_cards_html += generate_card_html(animal)

    # 4. Platzhalter im Template ersetzen
    final_html = template_content.replace("__REPLACE_CARDS__", all_cards_html)

    # 5. In 'animals.html' schreiben
    with open("animals.html", "w", encoding='utf-8') as f:
        f.write(final_html)

    print("Erfolg: 'animals.html' wurde erstellt.")


if __name__ == "__main__":
    main()