import sqlite3
import json

from models.animal import Animal
from models.location import Location
from models.customers import Customer

ANIMALS = [
    Animal(1, "George", "Dog", "Adopted", 2, 4),
    Animal(2, "Mike", "Cat", "Not Adopted", 1, 1),
    Animal(3, "Clifford", "Dog", "Adopted", 2, 1)
]


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address
        FROM animal a
        JOIN location l
            ON l.id = a.location_id
        JOIN customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['customer_id'],
                            row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])

            animal.location = location.__dict__

            animal.customer = customer.__dict__

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


# Function with a single parameter
def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Animal
        WHERE id = ?
        """, ( id, ))
        
def get_animals_by_location(location_id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.location_id = ?            
        """, ( location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['customer_id'], row['location_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def get_animals_by_status(status):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row 
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'], row['status'], row['customer_id'], row['location_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)


def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                customer_id = ?,
                location_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'], new_animal['status'], new_animal['customer_id'], new_animal['location_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def create_animal(new_animal):
        with sqlite3.connect("./kennel.db") as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO Animal
                ( name, breed, status, customer_id, location_id )
            VALUES
                ( ?, ?, ?, ?, ?);
            """, (new_animal['name'], new_animal['breed'], new_animal['treatment'], new_animal['customerId'], new_animal['locationId'], ))

            id = db_cursor.lastrowid

            new_animal['id'] = id

        return json.dumps(new_animal)
