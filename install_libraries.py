def install_libraries():
    import subprocess
    import sys

    # List of libraries to be installed
    libraries = [
        "matplotlib",      # For plotting and visualization
        "mpl_toolkits.mplot3d", # For 3D plotting
        "astropy",         # For astronomical calculations
        "astroquery"       # For querying astronomical databases
    ]

    # Function to install each library
    for lib in libraries:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    print("All libraries have been installed.")
