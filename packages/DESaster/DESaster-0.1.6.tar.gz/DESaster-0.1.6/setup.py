from distutils.core import setup

setup(
    # Application name:
    name="DESaster",

    # Version number (initial):
    version="0.1.6",

    # Application author details:
    author="Scott Miles",
    author_email="milessb@uw.edu",

    # Packages
    packages=["desaster"],
    
    # Package data
    package_data={'desaster': ['config/hazus_building_lookup_tables.xlsx']},

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/milessb/DESaster"


)