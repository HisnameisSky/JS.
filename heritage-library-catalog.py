import json

raw_catalog_cards = [
    "From a Buick 8 | King, Stephen | 2002 | Shelf K7",
    "The Shining | King, Stephen | 1977 | Shelf K1",
    "The Stand | King, Stephen | 1978 | Shelf K2",
    "It | King, Stephen | 1986 | Shelf K3",
    "Misery | King, Stephen | 1987 | Shelf K4",
    "Do Androids Dream of Electric Sheep? | Dick, Philip K. | 1968 | Shelf D5",
    "I, Robot | Asimov, Isaac | 1950 | Shelf A8",
    "Foundation | Asimov, Isaac | 1951 | Shelf A9",
    "Dune | Herbert, Frank | 1965 | Shelf H3",
    "Neuromancer | Gibson, William | 1984 | Shelf G8",
    "Snow Crash | Stephenson, Neal | 1992 | Shelf S6",
    "The Martian | Weir, Andy | 2011 | Shelf W5",
    "Ender's Game | Card, Orson Scott | 1985 | Shelf C2",
    "The Hitchhiker's Guide to the Galaxy | Adams, Douglas | 1979 | Shelf A1",
    "Ready Player One | Cline, Ernest | 2011 | Shelf C7",
    "The Dark Tower: The Gunslinger | King, Stephen | 1982 | Shelf K5",
    # edge cases: missing data
    "Unknown Title |  | 1975 | Shelf X1",
    "Mysterious Manuscript | Unknown Author |  | Shelf Z9",
    "Ancient Scroll | Anonymous | 850 | ",
]


def parse_card(raw_string):
    parts = raw_string.split("|")
    trimmed_parts = [part.strip() for part in parts]

    title = trimmed_parts[0] if len(trimmed_parts) > 0 else ""
    author = trimmed_parts[1] if len(trimmed_parts) > 1 else ""
    year = trimmed_parts[2] if len(trimmed_parts) > 2 else ""
    location = trimmed_parts[3] if len(trimmed_parts) > 3 else ""

    parsed_year = "Unknown"
    if year:
        try:
            parsed_year = int(year)
        except ValueError:
            parsed_year = "Unknown"

    return {
        "title": title if title else "Unknown",
        "author": author if author else "Unknown",
        "year": parsed_year,
        "location": location if location else "Unknown",
    }


def parse_catalog(raw_cards):
    catalog = []
    for raw_card in raw_cards:
        catalog.append(parse_card(raw_card))
    return catalog


catalog = parse_catalog(raw_catalog_cards)


def find_by_author(catalog, author):
    search_term = author.lower()
    results = []
    for book in catalog:
        if search_term in book["author"].lower():
            results.append(book)
    return results


def group_by_decade(catalog):
    grouped = {}
    for book in catalog:
        if book["year"] == "Unknown":
            if "Unknown" not in grouped:
                grouped["Unknown"] = []
            grouped["Unknown"].append(book)
            continue

        decade = (book["year"] // 10) * 10
        decade_key = f"{decade}s"

        if decade_key not in grouped:
            grouped[decade_key] = []
        grouped[decade_key].append(book)

    return grouped


by_decade = group_by_decade(catalog)


def render_entry(entry):
    title = entry.get("title") or "Unknown"
    author = entry.get("author") or "Unknown"
    year = entry.get("year") or "Unknown"
    location = entry.get("location") or "Unknown"

    border = "-" * 25
    return f"{border}\nTitle: {title}\nAuthor: {author}\nYear: {year}\nLocation: {location}\n{border}"


print(render_entry(catalog[0]))


def validate_entry(entry):
    is_valid = True
    for key in ["title", "author", "year", "location"]:
        if key not in entry or not entry[key] or entry[key] == "Unknown":
            is_valid = False
            break
    return is_valid


def export_to_json(catalog):
    return json.dumps(catalog, indent=2)


def export_to_csv(catalog):
    header = "Title,Author,Year,Location"
    rows = []
    for entry in catalog:
        rows.append(
            f'"{entry["title"]}","{entry["author"]}",{entry["year"]},"{entry["location"]}"'
        )

    return header + "\n" + "\n".join(rows)


print(export_to_csv(catalog))
print(f"Total books: {len(catalog)}")
print(f"Total decade groups: {len(by_decade)}")

oldest_year = float("inf")
newest_year = 0

for book in catalog:
    if book["year"] != "Unknown":
        if book["year"] < oldest_year:
            oldest_year = book["year"]
        if book["year"] > newest_year:
            newest_year = book["year"]

print(f"Oldest Year: {int(oldest_year)}")
print(f"Newest Year: {newest_year}")
print(len(catalog))
print(len(by_decade))
print(int(oldest_year))
print(newest_year)