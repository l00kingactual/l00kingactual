from astroquery.vizier import Vizier
import matplotlib.pyplot as plt

def get_stars_in_constellation(constellation_name):
    v = Vizier(columns=['HIP', 'RAJ2000', 'DEJ2000', '_RA.icrs', '_DE.icrs'])
    result = v.query_constraints(catalog="I/239/hip_main", constellation=constellation_name)
    return result[0] if result else None

# Query stars in the specified constellation
constellation = "Ursa Minor"
stars = get_stars_in_constellation(constellation)

# Extracting RA, Dec, and HIP values
ra = stars['_RA.icrs']
dec = stars['_DE.icrs']
hip_numbers = stars['HIP']

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(ra, dec)

# Annotating each star with its HIP number
for i, hip in enumerate(hip_numbers):
    plt.annotate(str(hip), (ra[i], dec[i]))

plt.title(f'Constellation Star Chart: {constellation}')
plt.xlabel('Right Ascension (degrees)')
plt.ylabel('Declination (degrees)')
plt.grid(True)
plt.show()
