from astroquery.simbad import Simbad

# List all available VOTable fields
available_fields = Simbad.list_votable_fields()
print(available_fields)

'''

--NOTES--

1. The parameter filtername must correspond to an existing filter. Filters include: B,V,R,I,J,K.  They are checked by SIMBAD but not astroquery.simbad

2. Fields beginning with rvz display the data as it is in the database. Fields beginning with rv force the display as a radial velocity. Fields beginning with z force the display as a redshift

3. For each measurement catalog, the VOTable contains all fields of the first measurement. When applicable, the first measurement is the mean one.

Available VOTABLE fields:

bibcodelist(y1-y2)
biblio
cel
cl.g
coo(opt)
coo_bibcode
coo_err_angle
coo_err_maja
coo_err_mina
coo_qual
coo_wavelength
coordinates
dec(opt)
dec_prec
diameter
dim
dim_angle
dim_bibcode
dim_incl
dim_majaxis
dim_minaxis
dim_qual
dim_wavelength
dimensions
distance
distance_result
einstein
fe_h
flux(filtername)
flux_bibcode(filtername)
flux_error(filtername)
flux_name(filtername)
flux_qual(filtername)
flux_system(filtername)
flux_unit(filtername)
fluxdata(filtername)
gcrv
gen
gj
hbet
hbet1
hgam
id(opt)
ids
iras
irc
iso
iue
jp11
link_bibcode
main_id
measurements
membership
mesplx
mespm
mk
morphtype
mt
mt_bibcode
mt_qual
otype
otype(opt)
otypes
parallax
plx
plx_bibcode
plx_error
plx_prec
plx_qual
pm
pm_bibcode
pm_err_angle
pm_err_maja
pm_err_mina
pm_qual
pmdec
pmdec_prec
pmra
pmra_prec
pos
posa
propermotions
ra(opt)
ra_prec
rot
rv_value
rvz_bibcode
rvz_error
rvz_qual
rvz_radvel
rvz_type
rvz_wavelength
sao
sp
sp_bibcode
sp_nature
sp_qual
sptype
td1
typed_id
ubv
uvby
uvby1
v*
velocity
xmm
z_value
For more information on a field:
Simbad.get_field_description ('field_name')
Currently active VOTABLE fields:
 ['main_id', 'coordinates']
None
'''