from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pymysql
from py2neo import Graph, Node

# Initialize Flask
app = Flask(__name__)

# Initialize MySQL
mysql_conn = pymysql.connect(host='localhost', user='root', password='@00e54m1sf1t?', db='astronomy')

# Initialize Neo4j
graph = Graph("bolt://brightstar:7687", auth=("neo4j", "@00e54m1sf1t?"))

# Web scraping function
def scrape_wikipedia_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # Extract required data (Placeholder)
    return {}

@app.route('/fetch_planet_data/<planet_name>', methods=['GET'])
def fetch_planet_data(planet_name):
    # Scrape Wikipedia
    data = scrape_wikipedia_page(f"https://en.wikipedia.org/wiki/{planet_name}")

    # Insert into MySQL
    with mysql_conn.cursor() as cursor:
        sql = "INSERT INTO planets (name, description, image_url, vrml_url) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data.get('name'), data.get('description'), data.get('image_url'), data.get('vrml_url')))
    mysql_conn.commit()

    # Insert into Neo4j
    planet_node = Node("Planet", name=data.get('name'), description=data.get('description'), image_url=data.get('image_url'), vrml_url=data.get('vrml_url'))
    graph.create(planet_node)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
