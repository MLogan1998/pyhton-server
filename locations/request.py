import json
import sqlite3

from models.location import Location

LOCATIONS = [
    Location(1, 'main', 'address')
]

def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        locations = []
        
        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)
    
    return json.dumps(locations)



def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l 
        WHERE l.id = ?           
        """, ( id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

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
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Location
        WHERE id = ?
        """, ( id, ))


def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            LOCATIONS[index] = Location(new_location["id"], new_location["name"], new_location["city"])
            break
