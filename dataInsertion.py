def insert_into_mysql(data, table_name):
    connection = mysql_connection()
    cursor = connection.cursor()
    
    sql = f"INSERT INTO {table_name} (name, description, image_url, vrml_url, wikipedia_url) VALUES (%s, %s, %s, %s, %s)"
    val = (data['name'], data['description'], data['image_url'], data['vrml_url'], data['wikipedia_url'])
    
    cursor.execute(sql, val)
    connection.commit()


# neo4j
def insert_into_neo4j(data, label):
    node = Node(label, name=data['name'], description=data['description'], image_url=data['image_url'], vrml_url=data['vrml_url'], wikipedia_url=data['wikipedia_url'])
    graph.create(node)
