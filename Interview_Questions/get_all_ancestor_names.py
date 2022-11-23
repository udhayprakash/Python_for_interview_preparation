person = {
    "name": "Pebbles",
    "mother": {"name": "Edna", "father": {"name": "joe"}, "mother": {"name": "jane"}},
    "father": {
        "name": "Ed",
        "father": {"name": "bob"},
        "mother": {"name": "katherine"},
    },
}

["Bob"]


def getAllNamesOfAncestors(p, relatives=None):
    if not p:
        return []
    if not relatives:
        relatives = []

    if not "name" in p:
        return []

    relatives.append(p["name"])

    if "mother" in p:
        getAllNamesOfAncestors(p["mother"], relatives)

    if "father" in p:
        getAllNamesOfAncestors(p["father"], relatives)

    return relatives


print(getAllNamesOfAncestors(person))  # ['Edna, joe, jane, bob']
