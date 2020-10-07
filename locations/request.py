LOCATIONS = [
    {
        "id": 1,
        "name": "Neyland Stadium",
        "city": "Knoxville",
    },
    {
        "id": 2,
        "name": "Nissan Stadium",
        "city": "Nashville",
    },
    {
        "id": 3,
        "name": "Red Rocks",
        "city": "Denver",
    }
]

def get_all_locations():
    return LOCATIONS


def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
