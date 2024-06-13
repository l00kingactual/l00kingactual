import subprocess

def install_packages(package_list):
    for package in package_list:
        subprocess.check_call(["python", '-m', 'pip', 'install', package])

# List of popular Python astronomy libraries
astronomy_libraries = ['astropy', 'astroquery', 'astroML', 'PyAstronomy', 'astroscrappy', 'astroplan', 'photutils', 'specutils', 'sunpy', 'astroalign']

# Install popular Python astronomy libraries
install_packages(astronomy_libraries)
