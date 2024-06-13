from astropy.coordinates import get_body
from astropy.time import Time

earth_coords = get_body('earth', Time.now())

from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

observation_time = Time.now()  # or Time('YYYY-MM-DD HH:MM:SS')

sun_coords = get_body('sun', observation_time, EarthLocation.of_site('Greenwich'))

from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

# Define the observation time
observation_time = Time.now()  # Replace with a specific time if needed

# Get the Sun's coordinates
sun_coords = get_body('sun', observation_time, EarthLocation.of_site('Greenwich'))

# sun_coords now contains the RA, Dec coordinates of the Sun at the specified time
print(sun_coords)
