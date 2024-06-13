'''Here is a Python function that outlines how one could perform such a query using Astropy and Astroquery. Note that this code will not execute in this environment due to the lack of internet access and the Astroquery module not being installed. You can run this function in your local Python environment where you have Astropy and Astroquery installed:
'''

from astroquery.simbad import Simbad
from astropy import units as u
from astropy.table import vstack

def query_stars(distance_range):
    # Set up the query object for SIMBAD
    custom_simbad = Simbad()
    custom_simbad.add_votable_fields('distance', 'typed_id', 'otype', 'ra(d)', 'dec(d)', 'ids', 'constellation', 'mass', 'planet', 'plx')

    # Define the query range in light years, converting to parsecs
    distance_pc = [(d * u.lightyear).to(u.pc).value for d in distance_range]

    # Initialize the result table
    result_table = None

    # Query stars in the range of distances
    for distance in distance_pc:
        query_criteria = f'distance < {distance}'
        result = custom_simbad.query_criteria(query_criteria)
        if result is not None:
            if result_table is None:
                result_table = result
            else:
                result_table = vstack([result_table, result])  # Combine the results into a single table

    return result_table

# Example use case:
distance_range = [2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]
stars_data = query_stars(distance_range)

# Display the resulting data (this would display a table with the queried information)
print(stars_data)
