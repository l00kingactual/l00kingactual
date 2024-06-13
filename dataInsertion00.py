def insert_into_mysql(data, table_name):
    connection = mysql_connection()
    cursor = connection.cursor()
    
    sql = f"""INSERT INTO {table_name} (name, description, image_url, vrml_url, wikipedia_url,
              x_coordinate, y_coordinate, z_coordinate, radius, orbital_radius, orbital_speed,
              inclination, composition, density, color)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    val = (
        data['name'], data['description'], data['image_url'], data['vrml_url'], data['wikipedia_url'],
        data['x_coordinate'], data['y_coordinate'], data['z_coordinate'], data['radius'],
        data['orbital_radius'], data['orbital_speed'], data['inclination'], data['composition'],
        data['density'], data['color']
    )
    
    cursor.execute(sql, val)
    connection.commit()


# neo4j
def insert_into_neo4j(data, label):
    node = Node(label, **data)
    graph.create(node)
