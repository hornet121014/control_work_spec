from mysql.connector import Error
import service.connect as service

connection_db = service.connection()

def add_animal(table_name, kind_id, animal_name, animal_command, animal_birth):
    insert = f"""
    insert into {table_name} (kind_id, animal_name, animal_command, animal_birth) values  
    ({kind_id}, "{animal_name}", "{animal_command}", '{animal_birth}');
    """
    execute_query(connection_db, insert)

def execute_query_show(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        return data
    except Error as e:
        print(f"the error '{e}' occurred")

def show_commands(animal_name):
    show_command = f"""
    SELECT animal_command FROM dog WHERE animal_name = "{animal_name}"
    UNION
    SELECT animal_command FROM cat WHERE animal_name = "{animal_name}"
    UNION
    SELECT animal_command FROM hamster WHERE animal_name = "{animal_name}"
    UNION
    SELECT animal_command FROM horse WHERE animal_name = "{animal_name}"
    UNION
    SELECT animal_command FROM camel WHERE animal_name = "{animal_name}"
    UNION
    SELECT animal_command FROM donkey WHERE animal_name = "{animal_name}";      
    """
    data = execute_query_show(connection_db, show_command)
    print(f"Animal commands for {animal_name}:\n{data[0]}")

def teach_command(animal_name, command_new):
    find_animal = f"""
    SELECT p.pets_name, animal_name, animal_command FROM Dog
    JOIN Pets p ON kind_id = p.pets_id
    JOIN Animals a ON p.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}"
    UNION
    SELECT p.pets_name, animal_name, animal_command FROM Cat
    JOIN Pets p ON kind_id = p.pets_id
    JOIN Animals a ON p.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}"
    UNION
    SELECT p.pets_name, animal_name, animal_command FROM Hamster
    JOIN Pets p ON kind_id = p.pets_id
    JOIN Animals a ON p.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}"
    UNION
    SELECT pa.pack_animals_name, animal_name, animal_command FROM Horse
    JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
    JOIN Animals a ON pa.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}"
    UNION
    SELECT pa.pack_animals_name, animal_name, animal_command FROM Camel
    JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
    JOIN Animals a ON pa.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}"
    UNION
    SELECT pa.pack_animals_name, animal_name, animal_command FROM Donkey
    JOIN Pack_animals pa ON kind_id = pa.pack_animals_id
    JOIN Animals a ON pa.parent_id = a.animals_id
    WHERE animal_name = "{animal_name}";        
    """

    data = execute_query_show(connection_db, find_animal)

    teach_command = f"""
    UPDATE {data[0]} SET animal_command = CONCAT(animal_command, ", {command_new}") WHERE animal_name = "{animal_name}" 
    """

    execute_query(connection_db, teach_command)
    print(f"The command {command_new} has been successfully learned by the animal {animal_name}")


def get_animal_type(animal_type):
    kind_id = 0
    if animal_type.lower() == "dog" or animal_type.lower() == "horse":
        kind_id = 1
    elif animal_type.lower() == "cat" or animal_type.lower() == "camel":
        kind_id = 2
    elif animal_type.lower() == "hamster" or animal_type.lower() == "donkey":
        kind_id = 3
    else:
        print("unknown animal type!")
    return kind_id

def get_table(animal_type):
    table_name = None
    if animal_type.lower() == "dog":
        table_name = "dog"
    elif animal_type.lower() == "cat":
        table_name = "cat"
    elif animal_type.lower() == "hamster":
        table_name = "hamster"
    elif animal_type.lower() == "horse":
        table_name = "horse"
    elif animal_type.lower() == "camel":
        table_name = "camel"
    elif animal_type.lower() == "donkey":
        table_name = "donkey"
    else:
        print("table don't exists!")
    return table_name

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"the error '{e}' occurred")

def execute_query_select(connection, table_name, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        print(f"\ntable {table_name}:")
        return data
    except Error as e:
        print(f"the error '{e}' occurred")


