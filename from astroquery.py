from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord
import astropy.units as u

# Set the Simbad timeout to 120 seconds
Simbad.TIMEOUT = 120  # Increase the timeout to 120 seconds
5
# Prompt the user for the radius of the search region in degrees
radius_deg = float(input("Enter the radius of the search region in degrees: "))

# Define the target coordinates (replace with appropriate coordinates)
earth_coords = SkyCoord(ra=0, dec=0, unit=(u.deg, u.deg))  # Example coordinates

# Query the Simbad database for objects within the specified angular radius
result_table = Simbad.query_region(earth_coords, radius=radius_deg * u.deg)

# Print the results
if result_table:
    for row in result_table:
        # Extract and print relevant information
        # ...
        print("-" * 50)
else:
    print("No objects found within the specified radius.")
    
from astroquery.simbad import Simbad
from astropy.coordinates import SkyCoord, solar_system_ephemeris, get_body_barycentric
from astropy.time import Time
import astropy.units as u

# Prompt the user for the radius of the search region in degrees
radius_deg = float(input("Enter the radius of the search region in degrees: "))

# Set the solar system ephemeris to 'builtin'
solar_system_ephemeris.set('builtin')

# Use the barycenter of the solar system as a reference point
earth_coords = get_body_barycentric('earth', Time.now())

# Query the Simbad database for objects within the specified angular radius
result_table = Simbad.query_region(earth_coords, radius=radius_deg * u.deg)

# Print the results
if result_table:
    for row in result_table:
        # Extract relevant information
        object_name = row['MAIN_ID']
        ra = row['RA']
        dec = row['DEC']
        
        # Print the information
        print(f"Object: {object_name}")
        print(f"RA: {ra}")
        print(f"Dec: {dec}")

        # Additional information (constellation and associated planets) can be obtained if available.
        # ...

    print("-" * 50)
else:
    print("No objects found within the specified radius.")