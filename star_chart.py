import matplotlib.pyplot as plt

# Data for the stars in the constellation (RA in hours, Dec in degrees)
stars = {
    "Star1": {"ra": ra_value1, "dec": dec_value1},
    "Star2": {"ra": ra_value2, "dec": dec_value2},
    # Add more stars as needed
}

ra = [stars[star]["ra"] for star in stars]
dec = [stars[star]["dec"] for star in stars]

plt.figure(figsize=(8, 5))
plt.scatter(ra, dec)

# Optional: Annotate each star
for star in stars:
    plt.annotate(star, (stars[star]["ra"], stars[star]["dec"]))

plt.title('Constellation Star Chart')
plt.xlabel('Right Ascension (hours)')
plt.ylabel('Declination (degrees)')
plt.grid(True)
plt.show()
