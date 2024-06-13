from astroquery.vizier import Vizier

def get_stars_in_constellation(constellation_name):
    v = Vizier(columns=['HIP', 'RAJ2000', 'DEJ2000', '_RA.icrs', '_DE.icrs'])
    result = v.query_constraints(catalog="I/239/hip_main", constellation=constellation_name)
    return result[0] if result else None

# Example usage:
constellation = "Ursa Minor"
stars = get_stars_in_constellation(constellation)
print(stars)


import matplotlib.pyplot as plt

# Extracting RA, Dec, and HIP values from your data
ra = [0.00089921, 0.00426461, 0.00502431, 0.00862924, 0.00997344, ...]  # Add all RA values
dec = [1.08900875, -19.49883971, 38.85927901, -51.89354573, -40.59120235, ...]  # Add all Dec values
hip_numbers = [1, 2, 3, 4, 5, ...]  # Add all HIP numbers

plt.figure(figsize=(10, 6))
plt.scatter(ra, dec)

# Optional: Annotate each star with its HIP number
for i, hip in enumerate(hip_numbers):
    plt.annotate(hip, (ra[i], dec[i]))

plt.title('Constellation Star Chart')
plt.xlabel('Right Ascension (degrees)')
plt.ylabel('Declination (degrees)')
plt.grid(True)
plt.show()
