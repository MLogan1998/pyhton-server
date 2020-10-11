from models.location import Location

LOCATIONS = [
    Location(1, "Neyland Stadium", "Knoxville"),
    Location(2, "Nissan Stadium", "Nashville"),
    Location(3, "Red Rocks", "Denver")
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
        if location.id == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1].id

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    new_location = Location(location["id"], location["name"], location["city"])
    LOCATIONS.append(new_location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            location_index = index
        
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            LOCATIONS[index] = Location(new_location["id"], new_location["name"], new_location["city"])
            break
