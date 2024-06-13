from astroquery.simbad import Simbad

def get_stars_in_constellation(constellation_name):
    result_table = Simbad.query_object(f"region({constellation_name})")
    return result_table

# Example usage:
constellation = "Ursa Minor"
stars = get_stars_in_constellation(constellation)
print(stars)
