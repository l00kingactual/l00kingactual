from bs4 import BeautifulSoup
import requests

class ArchaeologicalSites:
    def __init__(self):
        self.data = self.fetch_data()

    def fetch_data(self):
        url = 'https://en.wikipedia.org/wiki/List_of_archaeological_sites_by_continent_and_age'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {}
        current_h2 = None
        current_h3 = None
        current_h4 = None

        for tag in soup.find_all(['h2', 'h3', 'h4', 'ul']):
            if tag.name == 'h2':
                current_h2 = tag.text.strip()
                data[current_h2] = {}
                current_h3 = None
                current_h4 = None
            elif tag.name == 'h3':
                current_h3 = tag.text.strip()
                data[current_h2][current_h3] = {}
                current_h4 = None
            elif tag.name == 'h4':
                current_h4 = tag.text.strip()
                data[current_h2][current_h3][current_h4] = []
            elif tag.name == 'ul':
                list_data = []
                for li_tag in tag.find_all('li'):
                    list_data.append(li_tag.text.strip())
                
                if current_h4:
                    data[current_h2][current_h3][current_h4] = list_data
                elif current_h3:
                    data[current_h2][current_h3] = list_data
                else:
                    data[current_h2] = list_data
            
            self.data = data

        return data  # This should be at the same indentation level as the for-loop, not inside it.

def __init__(self):
    self.data = self.fetch_data()



from pprint import pprint

class ArchaeologicalSites:
    def __init__(self):
        # Your initialization code here
        self.data = {}  # or however you initialize it

    # Define the debug method inside your class
    def debug_data_structure(self):
        pprint(self.data)
        print("Type of self.data:", type(self.data))

        if self.data:  # Check if dictionary is not empty
            first_key = list(self.data.keys())[0]
            print("Type of first key's value:", type(self.data[first_key]))

# Initialize an instance
archaeological_sites = ArchaeologicalSites()
# After populating data
archaeological_sites.debug_data_structure()  # This should now work


# Instantiate the class
# Somewhere in your code where you have an instance of the class
#archaeological_sites = ArchaeologicalSites()  # This assumes your data fetching methods are called within __init__ or have already been called.
#archaeological_sites.debug_data_structure()


from bs4 import BeautifulSoup
import webbrowser

class ArchaeologicalSitesHTMLGenerator:
    def __init__(self, archaeological_sites_data):
        self.data = archaeological_sites_data
    
    def generate_html(self):
        with open('archaeological_sites.html', 'w', encoding='utf-8') as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html lang="en">\n')
            f.write('<head>\n')
            f.write('  <meta charset="UTF-8">\n')
            f.write('  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet">\n')
            f.write('  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>\n')
            f.write('  <title>Archaeological Sites</title>\n')
            f.write('</head>\n')
            f.write('<body>\n')
            
            # Write the class description
            f.write('<h1 class="text-center">Class: ArchaeologicalSites</h1>\n')
            f.write('<p>This class is responsible for fetching and storing archaeological site data.</p>\n')
            
            # Write the actual data
            f.write('<h1>Data</h1>\n')
            for continent, age_list in self.data.items():
                f.write(f'  <h2>{continent}</h2>\n')
                for age in age_list:  # If age_list contains string elements representing ages
                    f.write(f'    <h3>{age}</h3>\n')
                    # The rest of your logic, tailored to what data exists under each 'age'

                    f.write('    <ul class="list-group">\n')
                    for site in sites:
                        f.write(f'      <li class="list-group-item">{site}</li>\n')
                    f.write('    </ul>\n')

            
            f.write('</body>\n')
            f.write('</html>\n')
            
# Instantiate the ArchaeologicalSites class (Assuming this is defined elsewhere)
archaeological_sites = ArchaeologicalSites()

from pprint import pprint

def debug_data_structure(self):
    pprint(self.data)
    print("Type of self.data:", type(self.data))

    first_key = list(self.data.keys())[0]
    print("Type of first key's value:", type(self.data[first_key]))



'''
# Instantiate the HTML generator class and generate the HTML file
html_generator = ArchaeologicalSitesHTMLGenerator(archaeological_sites.data)
html_generator.generate_html()

# Optional: Pretty-print the generated HTML file
with open('archaeological_sites.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

with open('archaeological_sites.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# Open the generated HTML page in Chrome
try:
    webbrowser.get("chrome").open('archaeological_sites.html')
except webbrowser.Error:
    print("Could not locate runnable browser.")
'''