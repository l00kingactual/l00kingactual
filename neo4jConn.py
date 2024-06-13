from py2neo import Graph

try:
    graph = Graph("bolt://brightstar:7687", auth=("neo4j", "@00e54m1sf1t?"))
    graph.run("USE ouchAstronomy MATCH (n) RETURN n LIMIT 1")  # Test query with database specified
    print("Neo4j connection to ouchAstronomy successful.")
except Exception as e:
    print(f"Neo4j connection failed. Error: {e}")
