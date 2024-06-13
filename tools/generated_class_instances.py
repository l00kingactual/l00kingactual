from class_definition import ArchaeologicalSites, Continent, Age

Stone_Age = Age('Stone Age', ["Site 1", "Site 2"])
Bronze_Age = Age('Bronze Age', ["Site 3"])
Iron_Age = Age('Iron Age', ["Site 4"])
Africa = Continent('Africa', [Stone_Age, Bronze_Age])
Europe = Continent('Europe', [Iron_Age])
archaeological_sites = ArchaeologicalSites([Africa, Europe])
