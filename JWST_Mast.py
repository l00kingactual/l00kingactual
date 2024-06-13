from astroquery.mast import Mast
from astroquery.mast import Observations

# Define your search criteria
object_name = "M31"  # The Andromeda Galaxy, for example
radius_deg = 1.0  # Search radius in degrees

# Query MAST for your object
obsTable = Mast.query_object(object_name, radius=radius_deg)

# Filter the results to only include JWST data (optional)
jwst_data = obsTable[obsTable['obs_collection'] == 'JWST']

# If you want to further filter by specific instruments or configurations, you can do so here
# For example, to only include NIRCam data:
# jwst_data = jwst_data[jwst_data['instrument_name'] == 'NIRCam']


# Filter the results to only include JWST data
jwst_data = obsTable[obsTable['obs_collection'] == 'JWST']

# Further filter to only include NIRSpec data
# jwst_data = jwst_data[jwst_data['instrument_name'] == 'NIRSpec']

# Fetch the list of data product IDs for your filtered results
data_products = Observations.get_product_list(jwst_data)

# Download the FITS files
# This will download all data products associated with each observation
# To download only specific types of data products, you can further filter 'data_products'
Observations.download_products(data_products, productSubGroupDescription=["SCIENCE"], extension="fits")

