from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack  # This is the missing import

custom_simbad = Simbad()
custom_simbad.TIMEOUT = 120  # Set timeout to 120 seconds

def setup_simbad_query_fields():
    # Initialize SIMBAD with default fields
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('distance', 'typed_id', 'otype', 'ra(d)', 'dec(d)', 'ids', 'flux(B)', 'flux(V)', 'plx', 'pm')

    # Return the customized SIMBAD object
    return custom_simbad

def query_stars(distance_range):
    # Setup SIMBAD with the desired fields
    custom_simbad = setup_simbad_query_fields()

    # Convert distance range from light years to parsecs
    distance_pc = [(d * u.lightyear).to(u.pc).value for d in distance_range]

    # Initialize the result table
    result_table = None

    # Query SIMBAD for each distance in the range
    for distance in distance_pc:
        query_criteria = f'distance < {distance}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Define the distance range
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

def query_stars_with_plx(distance_range):
    # Setup SIMBAD with the desired fields
    custom_simbad = setup_simbad_query_fields()

    # Initialize the result table
    result_table = None

    # Convert distance range from light years to parsecs, then to parallax
    for distance_ly in distance_range:
        distance_pc = (distance_ly * u.lightyear).to(u.pc).value
        parallax_mas = 1000 / distance_pc  # Parallax in milliarcseconds

        # Query SIMBAD for each parallax value in the range
        query_criteria = f'plx > {parallax_mas}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Example use case
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]
query_stars_with_plx(distance_range)