from setuptools import setup, find_packages
from os.path import join, dirname
import EntityResolution

setup(
    name='EntityResolution',
    version=EntityResolution.__version__,
    packages=find_packages(),
    scripts=['mainMenu.py','searchTwitterUsers.py','getFollowers.py', 'EntityResolution.py'],

    # Project uses these distributions which may need to be installed
    install_requires=['MySQL-python'],
    setup_requires = ['MySQL-python'],

    # metadata for upload to PyPI
    author= 'Corren McCoy',
    author_email='cmccoy@cs.odu.edu',
    description="Entity Disambiguation Between Online Social Networks",
    long_description=open(join(dirname(__file__), 'README.txt')).read(),

    license = "",
    keywords = "entity disambiguation LinkedIn Twitter",
    # project home page
    url = "http://www.cs.odu.edu/~cmccoy/entityresolution",

    entry_points={
        'console_scripts': 
            ['EntityResolution = EntityResolution:print_message']
        }

    )