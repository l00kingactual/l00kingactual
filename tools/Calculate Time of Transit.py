from datetime import datetime
from math import degrees, radians, sin, cos, asin
import ephem  # Install with pip install pyephem

def calculate_LST(longitude, date_time):
    observer = ephem.Observer()
    observer.lon = str(longitude)
    observer.date = date_time
    lst = observer.sidereal_time()
    return degrees(lst)  # Convert radians to degrees

def calculate_HA(LST, RA):
    return LST - RA

def calculate_altitude(Dec, Latitude, HA):
    Dec, Latitude, HA = radians(Dec), radians(Latitude), radians(HA)
    altitude = degrees(asin(sin(Dec) * sin(Latitude) + cos(Dec) * cos(Latitude) * cos(HA)))
    return altitude

# Example usage
longitude = -122.0838  # Longitude for Mountain View, CA
date_time = datetime.utcnow()  # Current date-time in UTC
RA = 10.684  # RA for Polaris in degrees
Dec = 89.2641  # Dec for Polaris in degrees
Latitude = 37.3861  # Latitude for Mountain View, CA

LST = calculate_LST(longitude, date_time)
HA = calculate_HA(LST, RA)
altitude = calculate_altitude(Dec, Latitude, HA)

print(f"Local Sidereal Time: {LST} degrees")
print(f"Hour Angle: {HA} degrees")
print(f"Altitude: {altitude} degrees")
