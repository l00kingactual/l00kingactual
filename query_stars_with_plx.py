from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack

def setup_simbad_query_fields():
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('otype', 'ra(d)', 'dec(d)', 'flux(B)', 'flux(V)', 'plx', 'pm', 'ids', 'main_id')
    return custom_simbad

def query_stars_with_plx(distance_range):
    custom_simbad = setup_simbad_query_fields()
    result_table = None

    for distance_ly in distance_range:
        distance_pc = (distance_ly * u.lightyear).to(u.pc).value
        parallax_mas = 1000 / distance_pc  # Parallax in milliarcseconds

        query_criteria = f'plx > {parallax_mas}'
        result = custom_simbad.query_criteria(query_criteria)
        
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])

    return result_table

# Define the distance range
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Query stars within the specified range
stars_data = query_stars_with_plx(distance_range)

# Note: This code must be executed in an environment with internet access and the Astroquery library installed.
